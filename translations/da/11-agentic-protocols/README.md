# Brug af Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentic Protocols](../../../translated_images/da/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

Efterhånden som brugen af AI-agenter vokser, øges også behovet for protokoller, der sikrer standardisering, sikkerhed og understøtter åben innovation. I denne lektion vil vi gennemgå 3 protokoller, der søger at imødekomme dette behov - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduktion

I denne lektion vil vi dække:

• Hvordan **MCP** tillader AI-agenter at få adgang til eksterne værktøjer og data for at fuldføre brugeropgaver.

• Hvordan **A2A** muliggør kommunikation og samarbejde mellem forskellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige sprog-grænseflader til enhver hjemmeside, hvilket gør det muligt for AI-agenter at opdage og interagere med indholdet.

## Læringsmål

• **Identificere** det grundlæggende formål og fordelene ved MCP, A2A og NLWeb i konteksten af AI-agenter.

• **Forklare** hvordan hver protokol faciliterer kommunikation og interaktion mellem LLM'er, værktøjer og andre agenter.

• **Genkende** de forskellige roller, hver protokol spiller i opbygningen af komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åben standard, der tilbyder en standardiseret måde for applikationer at levere kontekst og værktøjer til LLM'er. Dette muliggør en "universal adapter" til forskellige datakilder og værktøjer, som AI-agenter kan forbinde til på en ensartet måde.

Lad os se på komponenterne i MCP, fordelene i forhold til direkte API-brug, og et eksempel på, hvordan AI-agenter kan bruge en MCP-server.

### MCPs Kernekomponenter

MCP fungerer på en **klient-server arkitektur** og kernekomponenterne er:

• **Hosts** er LLM-applikationer (for eksempel en kodeeditor som VSCode), som starter forbindelser til en MCP-server.

• **Klienter** er komponenter inden for host-applikationen, der opretholder en-til-en forbindelser med servere.

• **Servere** er letvægtsprogrammer, der eksponerer specifikke kapaciteter.

Inkluderet i protokollen er tre kernebegreber, som er kapaciteterne hos en MCP-server:

• **Værktøjer**: Det er diskrete handlinger eller funktioner, som en AI-agent kan kalde for at udføre en handling. For eksempel kan en vejrtjeneste tilbyde et "hent vejr"-værktøj, eller en e-handelsserver kan tilbyde et "køb produkt"-værktøj. MCP-servere annoncerer hvert værktøjs navn, beskrivelse og input/output-skema i deres kapacitetsliste.

• **Ressourcer**: Det er læse-only dataelementer eller dokumenter, som en MCP-server kan levere, og klienter kan hente dem efter behov. Eksempler inkluderer filindhold, databaseposter eller logfiler. Ressourcer kan være tekst (som kode eller JSON) eller binære (som billeder eller PDF'er).

• **Prompts**: Det er foruddefinerede skabeloner, der tilbyder foreslåede prompts, hvilket muliggør mere komplekse workflows.

### Fordele ved MCP

MCP tilbyder væsentlige fordele for AI-agenter:

• **Dynamisk Værktøjsopdagelse**: Agenter kan dynamisk modtage en liste over tilgængelige værktøjer fra en server sammen med beskrivelser af, hvad de gør. Dette står i kontrast til traditionelle API'er, der ofte kræver statisk kodning til integrationer, hvilket betyder, at enhver API-ændring nødvendiggør kodeopdateringer. MCP tilbyder en "integrer én gang"-tilgang, hvilket fører til større tilpasningsevne.

• **Interoperabilitet på tværs af LLM’er**: MCP fungerer på tværs af forskellige LLM'er, hvilket giver fleksibilitet til at skifte kerne-modeller for at evaluere bedre ydeevne.

• **Standardiseret Sikkerhed**: MCP inkluderer en standard autentificeringsmetode, der forbedrer skalerbarheden ved tilføjelse af adgang til yderligere MCP-servere. Dette er enklere end at håndtere forskellige nøgler og autentificeringstyper for forskellige traditionelle API'er.

### MCP Eksempel

![MCP Diagram](../../../translated_images/da/mcp-diagram.e4ca1cbd551444a1.webp)

Forestil dig, at en bruger ønsker at booke en flyrejse ved hjælp af en AI-assistent drevet af MCP.

1. **Forbindelse**: AI-assistenten (MCP-klienten) forbinder til en MCP-server leveret af et flyselskab.

2. **Værktøjsopdagelse**: Klienten spørger flyselskabets MCP-server: "Hvilke værktøjer har I tilgængelige?" Serveren svarer med værktøjer som "søg flyrejser" og "book flyrejser".

3. **Værktøjskald**: Du beder så AI-assistenten: "Søg efter en flyrejse fra Portland til Honolulu." AI-assistenten, med sin LLM, identificerer, at den skal kalde værktøjet "søg flyrejser" og sender relevante parametre (afgangssted, destination) til MCP-serveren.

4. **Udførelse og respons**: MCP-serveren, der fungerer som et omslag, foretager det faktiske kald til flyselskabets interne booking-API. Den modtager derefter flyinformationerne (f.eks. JSON-data) og sender det tilbage til AI-assistenten.

5. **Yderligere interaktion**: AI-assistenten præsenterer flymulighederne. Når du vælger en flyrejse, kan assistenten aktivere værktøjet "book flyrejse" på samme MCP-server for at fuldføre bookingen.

## Agent-til-Agent Protokol (A2A)

Mens MCP fokuserer på at forbinde LLM’er til værktøjer, går **Agent-til-Agent (A2A) protokollen** et skridt videre ved at muliggøre kommunikation og samarbejde mellem forskellige AI-agenter. A2A forbinder AI-agenter på tværs af forskellige organisationer, miljøer og teknologistakke for at fuldføre en fælles opgave.

Vi vil gennemgå komponenterne og fordelene ved A2A samt et eksempel på, hvordan det kan anvendes i vores rejseapplikation.

### A2A Kernekomponenter

A2A fokuserer på at muliggøre kommunikation mellem agenter og lade dem arbejde sammen om at fuldføre en delopgave for brugeren. Hver komponent i protokollen bidrager til dette:

#### Agentkort

Ligesom en MCP-server deler en liste over værktøjer, har et Agentkort:
- Agentens navn.
- En **beskrivelse af de generelle opgaver**, den udfører.
- En **liste over specifikke færdigheder** med beskrivelser for at hjælpe andre agenter (eller endda menneskelige brugere) med at forstå, hvornår og hvorfor de ville ønske at kalde den agent.
- Den **nuværende Endepunkt-URL** for agenten.
- Agentens **version** og **kapaciteter** såsom streaming-svar og push-notifikationer.

#### Agent Udfører

Agent Udføreren har ansvaret for at **videregive konteksten fra brugersamtalen til den fjernstyrede agent**; den fjernstyrede agent har brug for dette for at forstå den opgave, der skal udføres. I en A2A-server bruger en agent sin egen Large Language Model (LLM) til at fortolke indkommende forespørgsler og udføre opgaver ved hjælp af sine egne interne værktøjer.

#### Artefakt

Når en fjernstyret agent har fuldført den ønskede opgave, skabes dens arbejdsprodukt som et artefakt. Et artefakt **indeholder resultatet af agentens arbejde**, en **beskrivelse af, hvad der blev udført**, og **tekstkonteksten**, som sendes gennem protokollen. Efter artefaktet er sendt, lukkes forbindelsen til den fjernstyrede agent, indtil den igen er nødvendig.

#### Begivenhedskø

Denne komponent bruges til **at håndtere opdateringer og sende beskeder**. Den er især vigtig i produktionsmiljøer for agentiske systemer for at forhindre, at forbindelsen mellem agenter lukkes, før en opgave er fuldført, især når opgavens gennemførelse kan tage længere tid.

### Fordele ved A2A

• **Forbedret Samarbejde**: Det muliggør, at agenter fra forskellige leverandører og platforme kan interagere, dele kontekst og arbejde sammen, hvilket letter problemfri automatisering på tværs af traditionelt adskilte systemer.

• **Fleksibilitet i Modelvalg**: Hver A2A-agent kan vælge, hvilken LLM den bruger til at servicere sine forespørgsler, hvilket giver mulighed for optimerede eller fintunede modeller pr. agent, i modsætning til en enkelt LLM-forbindelse i visse MCP-scenarier.

• **Indbygget Autentificering**: Autentificering er integreret direkte i A2A-protokollen og giver en robust sikkerhedsramme for agent-interaktioner.

### A2A Eksempel

![A2A Diagram](../../../translated_images/da/A2A-Diagram.8666928d648acc26.webp)

Lad os udbygge vores rejsebookingscenarie, denne gang med A2A.

1. **Brugeranmodning til Multi-Agent**: En bruger interagerer med en "Rejseagent" som A2A-klient/agent, måske ved at sige: "Book venligst en hel tur til Honolulu i næste uge, inklusive fly, hotel og lejebil".

2. **Orkestrering af Rejseagenten**: Rejseagenten modtager denne komplekse anmodning. Den bruger sin LLM til at ræsonnere om opgaven og fastslår, at den skal interagere med andre specialiserede agenter.

3. **Inter-Agent Kommunikation**: Rejseagenten bruger derefter A2A-protokollen til at forbinde sig til underordnede agenter, såsom en "Flyselskab Agent," en "Hotel Agent" og en "Lejebil Agent," som er oprettet af forskellige virksomheder.

4. **Delegeret Opgaveudførelse**: Rejseagenten sender specifikke opgaver til disse specialiserede agenter (f.eks. "Find fly til Honolulu," "Book et hotel," "Lej en bil"). Hver af disse specialiserede agenter, der kører deres egne LLM'er og anvender deres egne værktøjer (som kunne være MCP-servere), udfører sin specifikke del af bookingen.

5. **Sammenfattet Respons**: Når alle underordnede agenter har fuldført deres opgaver, samler Rejseagenten resultaterne (flydetaljer, hotelbekræftelse, lejebilbooking) og sender et sammenhængende, chat-lignende svar tilbage til brugeren.

## Natural Language Web (NLWeb)

Websites har længe været den primære måde for brugere at få adgang til information og data på internettet.

Lad os se på de forskellige komponenter i NLWeb, fordelene ved NLWeb og et eksempel på, hvordan vores NLWeb fungerer ved at kigge på vores rejseapplikation.

### Komponenter i NLWeb

- **NLWeb Applikation (Kernens Servicekode)**: Systemet, der behandler naturlige sprogspørgsmål. Det forbinder de forskellige dele af platformen for at skabe svar. Du kan tænke på det som **motoren, der driver naturlige sprog-funktionaliteter** på en hjemmeside.

- **NLWeb Protokol**: Dette er et **grundlæggende sæt regler for naturlig sproginteraktion** med en hjemmeside. Den sender svar tilbage i JSON-format (ofte med Schema.org). Dens formål er at skabe et simpelt fundament for "AI Web," på samme måde som HTML gjorde det muligt at dele dokumenter online.

- **MCP Server (Model Context Protocol Endpoint)**: Hver NLWeb-installation fungerer også som en **MCP-server**. Det betyder, at den kan **dele værktøjer (som en “ask”-metode) og data** med andre AI-systemer. I praksis gør det websitet’s indhold og evner brugbare for AI-agenter, hvilket gør siden til en del af det bredere "agent-økosystem."

- **Indlejringsmodeller**: Disse modeller bruges til at **konvertere websideindhold til numeriske repræsentationer kaldet vektorer** (indlejringer). Disse vektorer fanger mening på en måde, som computere kan sammenligne og søge i. De gemmes i en særlig database, og brugerne kan vælge, hvilken indlejringsmodel de ønsker at bruge.

- **Vektor Database (Hentningsmekanisme)**: Denne database **gemmer indlejringer af websideindholdet**. Når nogen stiller et spørgsmål, tjekker NLWeb vektordatabasen for hurtigt at finde den mest relevante information. Den giver en hurtig liste over mulige svar, rangeret efter lighed. NLWeb fungerer med forskellige vektorlager-systemer som Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved Eksempel

![NLWeb](../../../translated_images/da/nlweb-diagram.c1e2390b310e5fe4.webp)

Tag vores rejsebookingswebsite igen, men denne gang drevet af NLWeb.

1. **Dataindtagelse**: Det eksisterende produktkatalog på rejsewebsitet (f.eks. flylister, hotelbeskrivelser, turistpakker) formateres ved hjælp af Schema.org eller indlæses via RSS-feeds. NLWebs værktøjer optager disse strukturerede data, skaber indlejringer og gemmer dem i en lokal eller fjern vektordatabase.

2. **Naturligt Sprogsspørgsmål (Menneske)**: En bruger besøger websitet og skriver i stedet for at navigere i menuer i en chatgrænseflade: "Find mig et familievenligt hotel i Honolulu med pool til næste uge".

3. **NLWeb Behandling**: NLWeb-applikationen modtager denne forespørgsel. Den sender forespørgslen til en LLM for forståelse og søger samtidig i sin vektordatabase efter relevante hoteltilbud.

4. **Præcise Resultater**: LLM hjælper med at fortolke søgeresultaterne fra databasen, identificerer de bedste matches baseret på kriterierne "familievenligt," "pool" og "Honolulu," og formaterer derefter et svar på naturligt sprog. Vigtigt er, at svaret henviser til faktiske hoteller fra websitet’s katalog og undgår opdigtede informationer.

5. **AI-Agent Interaktion**: Fordi NLWeb fungerer som en MCP-server, kan en ekstern AI-rejseagent også forbinde til denne hjemmesides NLWeb-instans. AI-agenten kan så bruge `ask` MCP-metoden til direkte at forespørge websitet: `ask("Er der nogen veganske restauranter i Honolulu-området anbefalet af hotellet?")`. NLWeb-instansen vil behandle dette, udnytte sin database med restaurantinformation (hvis indlæst), og returnere et struktureret JSON-svar.

### Har du flere spørgsmål om MCP/A2A/NLWeb?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine AI-agent-spørgsmål.

## Ressourcer

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->