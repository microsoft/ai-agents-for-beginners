# Kontekst-Engineering for AI-Agenter

[![Context Engineering](../../../translated_images/da/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

At forstå kompleksiteten af den applikation, du bygger en AI-agent til, er vigtigt for at skabe en pålidelig en. Vi skal bygge AI-agenter, der effektivt håndterer information for at imødekomme komplekse behov ud over prompt engineering.

I denne lektion vil vi se på, hvad kontekst-engineering er, og hvilken rolle det spiller i opbygningen af AI-agenter.

## Introduktion

Denne lektion vil dække:

• **Hvad kontekst-engineering er** og hvorfor det adskiller sig fra prompt engineering.

• **Strategier for effektiv kontekst-engineering**, herunder hvordan man skriver, vælger, komprimerer og isolerer information.

• **Almindelige kontekstfejl**, der kan spore din AI-agent af, og hvordan du løser dem.

## Læringsmål

Efter at have gennemført denne lektion vil du forstå, hvordan du kan:

• **Definere kontekst-engineering** og skelne det fra prompt engineering.

• **Identificere nøglekomponenterne i kontekst** i applikationer med store sprogmodeller (LLM).

• **Anvende strategier til at skrive, vælge, komprimere og isolere kontekst** for at forbedre agentens ydeevne.

• **Genkende almindelige kontekstfejl** såsom forgiftning, distraktion, forvirring og sammenstød, og implementere afbødningsteknikker.

## Hvad er kontekst-engineering?

For AI-agenter er konteksten det, der styrer planlægningen af en AI-agent til at tage bestemte handlinger. Kontekst-engineering er praksis med at sikre, at AI-agenten har den rette information til at fuldføre næste trin i opgaven. Kontekstvinduet er begrænset i størrelse, så som agentbyggere skal vi skabe systemer og processer til at håndtere tilføjelse, fjernelse og kondensering af information i kontekstvinduet.

### Prompt engineering vs. kontekst-engineering

Prompt engineering fokuserer på et enkelt sæt statiske instruktioner for effektivt at guide AI-agenter med et sæt regler. Kontekst-engineering handler om, hvordan man håndterer et dynamisk sæt informationer, inklusive den oprindelige prompt, for at sikre, at AI-agenten har det, den behøver over tid. Hovedideen ved kontekst-engineering er at gøre denne proces gentagelig og pålidelig.

### Typer af kontekst

[![Types of Context](../../../translated_images/da/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Det er vigtigt at huske, at kontekst ikke bare er én ting. Den information, som AI-agenten behøver, kan komme fra mange forskellige kilder, og det er op til os at sikre, at agenten har adgang til disse kilder:

De typer kontekst, en AI-agent måske skal håndtere, inkluderer:

• **Instruktioner:** Disse er som agentens "regler" – prompts, systembeskeder, få-skud-eksempler (der viser AI'en, hvordan man gør noget) og beskrivelser af værktøjer, den kan bruge. Her kombineres fokus fra prompt engineering med kontekst-engineering.

• **Viden:** Dette dækker fakta, information hentet fra databaser eller langtidshukommelse, som agenten har akkumuleret. Dette inkluderer integration af Retrieval Augmented Generation (RAG) system, hvis en agent behøver adgang til forskellige videnslagre og databaser.

• **Værktøjer:** Disse er definitioner af eksterne funktioner, API'er og MCP-servere, som agenten kan kalde, sammen med den feedback (resultater), den får ved at bruge dem.

• **Samtalehistorik:** Den igangværende dialog med en bruger. Som tiden går, bliver disse samtaler længere og mere komplekse, hvilket betyder, at de fylder plads i kontekstvinduet.

• **Brugerpræferencer:** Information lært om en brugers ønsker eller aferskede over tid. Disse kunne blive gemt og anvendt ved vigtige beslutninger for at hjælpe brugeren.

## Strategier til effektiv kontekst-engineering

### Planlægningsstrategier

[![Context Engineering Best Practices](../../../translated_images/da/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

God kontekst-engineering starter med god planlægning. Her er en tilgang, der vil hjælpe dig med at begynde at tænke over, hvordan du anvender konceptet kontekst-engineering:

1. **Definér klare resultater** - Resultaterne af opgaverne, som AI-agenter vil blive tildelt, skal defineres klart. Svar på spørgsmålet - "Hvordan vil verden se ud, når AI-agenten er færdig med sin opgave?" Med andre ord, hvilken ændring, information eller respons skal brugeren have efter interaktionen med AI-agenten.
2. **Kortlæg konteksten** - Når du har defineret AI-agentens resultater, skal du besvare spørgsmålet "Hvilken information behøver AI-agenten for at fuldføre denne opgave?". På denne måde kan du begynde at kortlægge, hvor informationen kan findes.
3. **Opret kontekst-pipelines** - Nu hvor du kender informationskilden, skal du besvare spørgsmålet "Hvordan vil agenten hente denne information?". Dette kan gøres på flere måder, herunder RAG, brug af MCP-servere og andre værktøjer.

### Praktiske strategier

Planlægning er vigtigt, men når information begynder at strømme ind i vores agents kontekstvindue, skal vi have praktiske strategier til at håndtere det:

#### Håndtering af kontekst

Mens noget information automatisk tilføjes til kontekstvinduet, handler kontekst-engineering om at tage en mere aktiv rolle i denne information, hvilket kan gøres ved flere strategier:

 1. **Agentens arbejdsblok**
 Dette tillader AI-agenten at tage noter om relevant information om den aktuelle opgave og brugerinteraktioner under en enkelt session. Dette bør eksistere uden for kontekstvinduet i en fil eller runtime-objekt, som agenten senere kan hente i løbet af sessionen, hvis nødvendigt.

 2. **Hukommelser**
 Arbejdsblokke er gode til at håndtere information uden for kontekstvinduet i en enkelt session. Hukommeler muliggør, at agenter kan gemme og hente relevant information over flere sessioner. Dette kan inkludere opsummeringer, brugerpræferencer og feedback til forbedringer i fremtiden.

 3. **Komprimering af kontekst**
  Når kontekstvinduet vokser og nærmer sig sin grænse, kan teknikker som summering og trimning anvendes. Dette inkluderer enten at bevare kun den mest relevante information eller fjerne ældre beskeder.
  
 4. **Multi-agent-systemer**
  Udvikling af multi-agent-systemer er en form for kontekst-engineering, fordi hver agent har sit eget kontekstvindue. Hvordan den kontekst deles og overføres til forskellige agenter, er en anden ting, man skal planlægge, når man bygger disse systemer.
  
 5. **Sandbox-miljøer**
  Hvis en agent skal køre kode eller behandle store mængder information i et dokument, kan dette optage mange tokens for at behandle resultaterne. I stedet for at have dette al lagret i kontekstvinduet, kan agenten bruge et sandbox-miljø, der kan køre denne kode og kun læse resultaterne og anden relevant information.
  
 6. **Runtime-tilstandsobjekter**
   Dette gøres ved at skabe informationscontainere til at håndtere situationer, hvor agenten skal have adgang til bestemt information. For en kompleks opgave vil dette muliggøre, at agenten lagrer resultaterne af hver delopgave trin for trin, så konteksten forbliver knyttet kun til den specifikke delopgave.

#### Undersøgelse af kontekst

Når du har anvendt en af disse strategier, er det værd at tjekke, hvad det næste modelkald faktisk modtog. Et nyttigt debugging-spørgsmål er:

> Indlæste agenten for meget kontekst, forkert kontekst eller manglede den kontekst, den havde brug for?

Du behøver ikke at logge rå prompts, værktøjsoutput eller hukommelsesindhold for at besvare det spørgsmål. Til produktion foretrækkes små kontekstinspektionsoptegnelser, som fanger tællinger, id'er, hashes og politikmærkater:

- **Udvælgelse:** Spor hvor mange kandidatdele, værktøjer eller hukommelser der blev overvejet, hvor mange der blev valgt, og hvilken regel eller score der forårsagede, at de andre blev filtreret fra.
- **Komprimering:** Registrér kildeområdet eller spor-id, opsummerings-id, et estimeret tokenantal før og efter komprimering, og om det rå indhold blev udelukket fra næste kald.
- **Isolering:** Notér hvilken delopgave, der kørte i en separat agent, session eller sandbox, hvilken begrænset opsummering der blev returneret, og om stort værktøjsoutput blev holdt uden for hovedagentens kontekst.
- **Hukommelse og RAG:** Gem dokument-id'er for hentning, hukommelses-id'er, scorer, valgte id'er og redigeringsstatus i stedet for fuld hentet tekst.
- **Sikkerhed og privatliv:** Foretræk hashes, id'er, token-spande og politikmærkater fremfor følsomme prompt-tekster, værktøjsargumenter, værktøjsresultater eller brugerhukommelseskroppe.

Målet er ikke at beholde mere kontekst. Det er at efterlade nok bevis, så en udvikler kan afgøre, hvilken kontekststrategi der kørte, og om det ændrede det næste modelkald på den tiltænkte måde.

### Eksempel på kontekst-engineering

Lad os sige, at vi vil have en AI-agent til at **"Booke mig en tur til Paris."**

• En simpel agent, der kun bruger prompt engineering, vil måske bare svare: **"Okay, hvornår vil du gerne rejse til Paris?**". Den behandlede kun dit direkte spørgsmål på det tidspunkt, hvor brugeren spurgte.

• En agent, der bruger de kontekst-engineeringsstrategier, der er gennemgået, vil gøre meget mere. Før den overhovedet svarer, kan dens system:

  ◦ **Tjekke din kalender** for ledige datoer (hente realtidsdata).

 ◦ **Huske tidligere rejsepræferencer** (fra langtidshukommelsen) som dit foretrukne flyselskab, budget eller om du foretrækker direkte fly.

 ◦ **Identificere tilgængelige værktøjer** til fly- og hotelbooking.

- Så kunne et eksempel på svar være: "Hej [Dit navn]! Jeg kan se, at du er ledig i første uge af oktober. Skal jeg lede efter direkte fly til Paris med [Foretrukket flyselskab] inden for dit sædvanlige budget på [Budget]?". Dette rigere, kontekstbevidste svar demonstrerer styrken ved kontekst-engineering.

## Almindelige kontekstfejl

### Kontekst-forgiftning

**Hvad det er:** Når en hallucination (falsk information genereret af LLM) eller en fejl kommer ind i konteksten og gentagne gange refereres til, hvilket får agenten til at forfølge umulige mål eller udvikle nonsens-strategier.

**Hvad man skal gøre:** Implementer **kontekstvalidering** og **karantæne**. Valider information, før den tilføjes til langtidshukommelsen. Hvis potentiel forgiftning opdages, start friske konteksttråde for at forhindre, at den dårlige information spreder sig.

**Rejsebooking-eksempel:** Din agent hallucinerer en **direkte flyvning fra en lille lokal lufthavn til en fjern international by**, som faktisk ikke tilbyder internationale flyvninger. Denne ikke-eksisterende flydetalje bliver gemt i konteksten. Senere, når du beder agenten om at booke, forsøger den konstant at finde billetter til denne umulige rute, hvilket fører til gentagne fejl.

**Løsning:** Implementer et trin, der **validerer flyvningens eksistens og ruter med en realtids-API** _før_ flydetaljen tilføjes til agentens arbejdskontekst. Hvis valideringen fejler, bliver den fejlagtige information "satte i karantæne" og ikke brugt yderligere.

### Kontekst-distraktion

**Hvad det er:** Når konteksten bliver så stor, at modellen fokuserer for meget på den opsamlede historie i stedet for at bruge det, den lærte under træning, hvilket fører til gentagende eller uhjælpsomme handlinger. Modeller kan begynde at lave fejl, selv før kontekstvinduet er fuldt.

**Hvad man skal gøre:** Brug **kontekst-summering**. Komprimer periodisk opsamlet information til kortere opsummeringer, der bevarer vigtige detaljer samtidig med, at redundant historie fjernes. Dette hjælper med at "nulstille" fokus.

**Rejsebooking-eksempel:** Du har diskuteret forskellige drømmerejsemål i lang tid, inklusive en detaljeret gengivelse af din rygsækrejse fra for to år siden. Når du endelig beder om at **"finde et billigt fly til næste måned,"** hænger agenten fast i de gamle, irrelevante detaljer og bliver ved med at spørge om din rygsækudrustning eller tidligere rejseplaner, mens den negligerer din nuværende forespørgsel.

**Løsning:** Efter et vist antal samtaleture eller når konteksten bliver for stor, bør agenten **opsummere de mest nylige og relevante dele af samtalen** – med fokus på dine aktuelle rejsedatoer og destination – og bruge denne kondenserede opsummering til det næste LLM-kald, mens den mindre relevante historiske chat kasseres.

### Kontekst-forvirring

**Hvad det er:** Når unødvendig kontekst, ofte i form af for mange tilgængelige værktøjer, får modellen til at generere dårlige svar eller kalde irrelevante værktøjer. Mindre modeller er især modtagelige for dette.

**Hvad man skal gøre:** Implementer **værktøjsstyring** ved brug af RAG-teknikker. Gem værktøjsbeskrivelser i en vektordatabase og vælg _kun_ de mest relevante værktøjer til hver specifik opgave. Forskning viser, at begrænsning af værktøjsudvalget til under 30 er effektivt.

**Rejsebooking-eksempel:** Din agent har adgang til dusinvis af værktøjer: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` osv. Du spørger, **"Hvad er den bedste måde at komme rundt i Paris på?"** På grund af det store antal værktøjer bliver agenten forvirret og forsøger at kalde `book_flight` _inden for_ Paris, eller `rent_car`, selvom du foretrækker offentlig transport, fordi værktøjsbeskrivelserne kan overlappe, eller den simpelthen ikke kan afgøre det bedste.

**Løsning:** Brug **RAG over værktøjsbeskrivelser**. Når du spørger om at komme rundt i Paris, henter systemet dynamisk _kun_ de mest relevante værktøjer som `rent_car` eller `public_transport_info` baseret på din forespørgsel og præsenterer en fokuseret "loadout" af værktøjer til LLM.

### Kontekst-sammenstød

**Hvad det er:** Når modstridende information eksisterer i konteksten, hvilket fører til inkonsistent ræsonnering eller dårlige endelige svar. Dette sker ofte, når information kommer i flere trin, og tidlige, forkerte antagelser forbliver i konteksten.

**Hvad man skal gøre:** Brug **kontekstbeskæring** og **aflastning**. Beskæring betyder at fjerne forældet eller modstridende information, efterhånden som nye detaljer ankommer. Aflastning giver modellen en separat "arbejdsblok"-arbejdsplads til at behandle information uden at rodet hovedkonteksten.


**Eksempel på rejsebooking:** Du fortæller oprindeligt din agent, **"Jeg vil gerne flyve økonomiklasse."** Senere i samtalen ombestemmer du dig og siger, **"Faktisk, for denne tur, lad os tage business class."** Hvis begge instruktioner forbliver i konteksten, kan agenten modtage modstridende søgeresultater eller blive forvirret over, hvilken præference der skal prioriteres.

**Løsning:** Implementer **kontekstbeskæring**. Når en ny instruktion modsiger en gammel, fjernes den ældre instruktion eller tilsidesættes eksplicit i konteksten. Alternativt kan agenten bruge en **scratchpad** til at afstemme modstridende præferencer, før der træffes en beslutning, hvilket sikrer, at kun den endelige, konsistente instruktion vejleder dets handlinger.

## Har du flere spørgsmål om kontekststyring?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få besvaret dine spørgsmål om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->