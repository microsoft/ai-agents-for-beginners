<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:04:06+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "da"
}
-->
# Brug af Agentiske Protokoller (MCP, A2A og NLWeb)

[![Agentiske Protokoller](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.da.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

Efterhånden som brugen af AI-agenter vokser, øges behovet for protokoller, der sikrer standardisering, sikkerhed og understøtter åben innovation. I denne lektion vil vi dække tre protokoller, der søger at imødekomme dette behov - Model Context Protocol (MCP), Agent to Agent (A2A) og Natural Language Web (NLWeb).

## Introduktion

I denne lektion vil vi dække:

• Hvordan **MCP** giver AI-agenter adgang til eksterne værktøjer og data for at fuldføre brugeropgaver.

• Hvordan **A2A** muliggør kommunikation og samarbejde mellem forskellige AI-agenter.

• Hvordan **NLWeb** bringer naturlige sproggrænseflader til enhver hjemmeside, hvilket gør det muligt for AI-agenter at opdage og interagere med indholdet.

## Læringsmål

• **Identificer** det primære formål og fordelene ved MCP, A2A og NLWeb i konteksten af AI-agenter.

• **Forklar** hvordan hver protokol faciliterer kommunikation og interaktion mellem LLM'er, værktøjer og andre agenter.

• **Genkend** de forskellige roller, hver protokol spiller i opbygningen af komplekse agentiske systemer.

## Model Context Protocol

**Model Context Protocol (MCP)** er en åben standard, der giver en standardiseret måde for applikationer at levere kontekst og værktøjer til LLM'er. Dette muliggør en "universel adapter" til forskellige datakilder og værktøjer, som AI-agenter kan forbinde til på en ensartet måde.

Lad os se på MCP's komponenter, fordelene sammenlignet med direkte API-brug og et eksempel på, hvordan AI-agenter kan bruge en MCP-server.

### MCP Kernekomponenter

MCP opererer på en **klient-server arkitektur**, og kernekomponenterne er:

• **Hosts** er LLM-applikationer (for eksempel en kodeeditor som VSCode), der starter forbindelserne til en MCP-server.

• **Klienter** er komponenter inden for host-applikationen, der opretholder en-til-en forbindelser med servere.

• **Servere** er letvægtsprogrammer, der tilbyder specifikke funktioner.

Protokollen inkluderer tre kerneprimitiver, som er MCP-serverens kapaciteter:

• **Værktøjer**: Dette er diskrete handlinger eller funktioner, som en AI-agent kan kalde for at udføre en opgave. For eksempel kan en vejrtjeneste tilbyde et "hent vejr"-værktøj, eller en e-handelsserver kan tilbyde et "køb produkt"-værktøj. MCP-servere annoncerer hvert værktøjs navn, beskrivelse og input/output-skema i deres kapacitetsliste.

• **Ressourcer**: Dette er skrivebeskyttede dataelementer eller dokumenter, som en MCP-server kan levere, og klienter kan hente dem efter behov. Eksempler inkluderer filindhold, databaseposter eller logfiler. Ressourcer kan være tekst (som kode eller JSON) eller binære (som billeder eller PDF'er).

• **Prompter**: Dette er foruddefinerede skabeloner, der giver foreslåede prompts, hvilket muliggør mere komplekse arbejdsgange.

### Fordele ved MCP

MCP tilbyder betydelige fordele for AI-agenter:

• **Dynamisk Værktøjsopdagelse**: Agenter kan dynamisk modtage en liste over tilgængelige værktøjer fra en server sammen med beskrivelser af, hvad de gør. Dette står i kontrast til traditionelle API'er, der ofte kræver statisk kodning for integrationer, hvilket betyder, at enhver API-ændring kræver kodeopdateringer. MCP tilbyder en "integrer én gang"-tilgang, hvilket fører til større tilpasningsevne.

• **Interoperabilitet på tværs af LLM'er**: MCP fungerer på tværs af forskellige LLM'er, hvilket giver fleksibilitet til at skifte kerne-modeller for at evaluere bedre ydeevne.

• **Standardiseret Sikkerhed**: MCP inkluderer en standard autentifikationsmetode, hvilket forbedrer skalerbarheden, når der tilføjes adgang til yderligere MCP-servere. Dette er enklere end at administrere forskellige nøgler og autentifikationstyper for forskellige traditionelle API'er.

### MCP Eksempel

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.da.png)

Forestil dig, at en bruger ønsker at booke en flyrejse ved hjælp af en AI-assistent drevet af MCP.

1. **Forbindelse**: AI-assistenten (MCP-klienten) forbinder til en MCP-server leveret af et flyselskab.

2. **Værktøjsopdagelse**: Klienten spørger flyselskabets MCP-server, "Hvilke værktøjer har du til rådighed?" Serveren svarer med værktøjer som "søg flyrejser" og "book flyrejser".

3. **Værktøjskald**: Du beder AI-assistenten, "Søg venligst efter en flyrejse fra Portland til Honolulu." AI-assistenten, ved hjælp af sin LLM, identificerer, at den skal kalde "søg flyrejser"-værktøjet og sender de relevante parametre (afgangssted, destination) til MCP-serveren.

4. **Udførelse og svar**: MCP-serveren, der fungerer som en wrapper, foretager det faktiske kald til flyselskabets interne booking-API. Den modtager derefter flyinformation (f.eks. JSON-data) og sender det tilbage til AI-assistenten.

5. **Yderligere interaktion**: AI-assistenten præsenterer flymulighederne. Når du vælger en flyrejse, kan assistenten kalde "book flyrejse"-værktøjet på den samme MCP-server og fuldføre bookingen.

## Agent-to-Agent Protocol (A2A)

Mens MCP fokuserer på at forbinde LLM'er til værktøjer, går **Agent-to-Agent (A2A) protokollen** et skridt videre ved at muliggøre kommunikation og samarbejde mellem forskellige AI-agenter. A2A forbinder AI-agenter på tværs af forskellige organisationer, miljøer og teknologiske stakke for at fuldføre en fælles opgave.

Vi vil undersøge komponenterne og fordelene ved A2A samt et eksempel på, hvordan det kunne anvendes i vores rejseapplikation.

### A2A Kernekomponenter

A2A fokuserer på at muliggøre kommunikation mellem agenter og få dem til at arbejde sammen om at fuldføre en delopgave for brugeren. Hver komponent i protokollen bidrager til dette:

#### Agentkort

Ligesom en MCP-server deler en liste over værktøjer, har et agentkort:
- Agentens navn.
- En **beskrivelse af de generelle opgaver**, den udfører.
- En **liste over specifikke færdigheder** med beskrivelser for at hjælpe andre agenter (eller endda menneskelige brugere) med at forstå, hvornår og hvorfor de vil kalde den agent.
- Den **aktuelle Endpoint URL** for agenten.
- Agentens **version** og **kapaciteter**, såsom streaming-svar og push-notifikationer.

#### Agentudfører

Agentudføreren er ansvarlig for **at videregive konteksten af brugerens chat til den eksterne agent**, som har brug for dette for at forstå den opgave, der skal udføres. På en A2A-server bruger en agent sin egen Large Language Model (LLM) til at analysere indkommende anmodninger og udføre opgaver ved hjælp af sine egne interne værktøjer.

#### Artefakt

Når en ekstern agent har fuldført den ønskede opgave, oprettes dens arbejdsprodukt som en artefakt. En artefakt **indeholder resultatet af agentens arbejde**, en **beskrivelse af, hvad der blev fuldført**, og den **tekstkontekst**, der sendes gennem protokollen. Efter artefakten er sendt, lukkes forbindelsen til den eksterne agent, indtil den igen er nødvendig.

#### Eventkø

Denne komponent bruges til **at håndtere opdateringer og videregive beskeder**. Den er især vigtig i produktion for agentiske systemer for at forhindre, at forbindelsen mellem agenter lukkes, før en opgave er fuldført, især når opgavens afslutning kan tage længere tid.

### Fordele ved A2A

• **Forbedret samarbejde**: Det muliggør, at agenter fra forskellige leverandører og platforme kan interagere, dele kontekst og arbejde sammen, hvilket letter problemfri automatisering på tværs af traditionelt adskilte systemer.

• **Fleksibilitet i modelvalg**: Hver A2A-agent kan beslutte, hvilken LLM den bruger til at håndtere sine anmodninger, hvilket giver mulighed for optimerede eller finjusterede modeller pr. agent, i modsætning til en enkelt LLM-forbindelse i nogle MCP-scenarier.

• **Indbygget autentifikation**: Autentifikation er integreret direkte i A2A-protokollen, hvilket giver en robust sikkerhedsramme for agentinteraktioner.

### A2A Eksempel

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.da.png)

Lad os udvide vores rejsebookingscenario, men denne gang ved hjælp af A2A.

1. **Brugeranmodning til multi-agent**: En bruger interagerer med en "Rejseagent" A2A-klient/agent, måske ved at sige: "Book venligst en hel rejse til Honolulu i næste uge, inklusive fly, hotel og lejebil."

2. **Orkestrering af rejseagent**: Rejseagenten modtager denne komplekse anmodning. Den bruger sin LLM til at ræsonnere om opgaven og afgøre, at den skal interagere med andre specialiserede agenter.

3. **Inter-agent kommunikation**: Rejseagenten bruger derefter A2A-protokollen til at forbinde til downstream-agenter, såsom en "Flyagent," en "Hotelagent" og en "Biludlejningsagent," der er oprettet af forskellige virksomheder.

4. **Delegeret opgaveudførelse**: Rejseagenten sender specifikke opgaver til disse specialiserede agenter (f.eks. "Find fly til Honolulu," "Book et hotel," "Lej en bil"). Hver af disse specialiserede agenter, der kører deres egne LLM'er og bruger deres egne værktøjer (som kunne være MCP-servere), udfører deres specifikke del af bookingen.

5. **Samlet svar**: Når alle downstream-agenter fuldfører deres opgaver, samler rejseagenten resultaterne (flydetaljer, hotelbekræftelse, biludlejningsbooking) og sender et omfattende, chat-stil svar tilbage til brugeren.

## Natural Language Web (NLWeb)

Hjemmesider har længe været den primære måde for brugere at få adgang til information og data på tværs af internettet.

Lad os se på de forskellige komponenter i NLWeb, fordelene ved NLWeb og et eksempel på, hvordan NLWeb fungerer ved at se på vores rejseapplikation.

### Komponenter i NLWeb

- **NLWeb-applikation (kernekode)**: Systemet, der behandler naturlige sprogspørgsmål. Det forbinder de forskellige dele af platformen for at skabe svar. Du kan tænke på det som **motoren, der driver de naturlige sprogfunktioner** på en hjemmeside.

- **NLWeb-protokol**: Dette er et **grundlæggende sæt regler for naturlig sproginteraktion** med en hjemmeside. Det sender svar tilbage i JSON-format (ofte ved hjælp af Schema.org). Formålet er at skabe et simpelt fundament for "AI-webben," på samme måde som HTML gjorde det muligt at dele dokumenter online.

- **MCP-server (Model Context Protocol Endpoint)**: Hver NLWeb-opsætning fungerer også som en **MCP-server**. Dette betyder, at den kan **dele værktøjer (som en "spørg"-metode) og data** med andre AI-systemer. I praksis gør dette hjemmesidens indhold og funktioner brugbare for AI-agenter, hvilket gør siden til en del af det bredere "agent-økosystem."

- **Embedding-modeller**: Disse modeller bruges til at **konvertere hjemmesideindhold til numeriske repræsentationer kaldet vektorer** (embeddings). Disse vektorer fanger betydning på en måde, som computere kan sammenligne og søge. De gemmes i en speciel database, og brugere kan vælge, hvilken embedding-model de vil bruge.

- **Vektordatabase (søgemekanisme)**: Denne database **gemmer embeddings af hjemmesideindholdet**. Når nogen stiller et spørgsmål, tjekker NLWeb vektordatabasen for hurtigt at finde den mest relevante information. Den giver en hurtig liste over mulige svar, rangeret efter lighed. NLWeb fungerer med forskellige vektorlagringssystemer såsom Qdrant, Snowflake, Milvus, Azure AI Search og Elasticsearch.

### NLWeb ved Eksempel

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.da.png)

Overvej vores rejsebookingside igen, men denne gang drevet af NLWeb.

1. **Dataindsamling**: Rejsehjemmesidens eksisterende produktkataloger (f.eks. flylister, hotelbeskrivelser, turpakker) formateres ved hjælp af Schema.org eller indlæses via RSS-feeds. NLWeb's værktøjer indlæser disse strukturerede data, opretter embeddings og gemmer dem i en lokal eller fjern vektordatabase.

2. **Naturligt sprogspørgsmål (menneske)**: En bruger besøger hjemmesiden og, i stedet for at navigere i menuer, skriver i en chatgrænseflade: "Find et familievenligt hotel i Honolulu med pool til næste uge."

3. **NLWeb-behandling**: NLWeb-applikationen modtager dette spørgsmål. Den sender spørgsmålet til en LLM for forståelse og søger samtidig i sin vektordatabase efter relevante hotellister.

4. **Præcise resultater**: LLM hjælper med at tolke søgeresultaterne fra databasen, identificere de bedste match baseret på "familievenligt," "pool" og "Honolulu"-kriterier og formaterer derefter et naturligt sprog-svar. Vigtigt er det, at svaret refererer til faktiske hoteller fra hjemmesidens katalog og undgår opfundne oplysninger.

5. **AI-agent interaktion**: Fordi NLWeb fungerer som en MCP-server, kunne en ekstern AI-rejseagent også forbinde til denne hjemmesides NLWeb-instans. AI-agenten kunne derefter bruge `ask` MCP-metoden til direkte at spørge hjemmesiden: `ask("Er der nogen veganske restauranter i Honolulu-området anbefalet af hotellet?")`. NLWeb-instansen ville behandle dette, udnytte sin database med restaurantinformation (hvis indlæst) og returnere et struktureret JSON-svar.

### Har du flere spørgsmål om MCP/A2A/NLWeb?

Deltag i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Ressourcer

- [MCP for begyndere](https://aka.ms/mcp-for-beginners)  
- [MCP-dokumentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb-repo](https://github.com/nlweb-ai/NLWeb)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.