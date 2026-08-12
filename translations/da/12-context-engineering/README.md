# Kontekstengineering for AI-agenter

[![Kontekstengineering](../../../translated_images/da/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

Det er vigtigt at forstå kompleksiteten af den applikation, du bygger en AI-agent til, for at skabe en pålidelig agent. Vi skal bygge AI-agenter, der effektivt håndterer information for at imødekomme komplekse behov ud over promptengineering.

I denne lektion vil vi se på, hvad kontekstengineering er, og hvilken rolle det spiller i opbygningen af AI-agenter.

## Introduktion

Denne lektion vil dække:

• **Hvad kontekstengineering er** og hvorfor det adskiller sig fra promptengineering.

• **Strategier for effektiv kontekstengineering**, herunder hvordan man skriver, vælger, komprimerer og isolerer information.

• **Almindelige kontekstfejl**, som kan få din AI-agent til at fejle, og hvordan man retter dem.

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

• **Definere kontekstengineering** og skelne det fra promptengineering.

• **Identificere nøglekomponenterne i kontekst** i Large Language Model (LLM) applikationer.

• **Anvende strategier til at skrive, vælge, komprimere og isolere kontekst** for at forbedre agentens ydeevne.

• **Genkende almindelige kontekstfejl** såsom forgiftning, distraktion, forvirring og konflikt, og implementere afhjælpningsteknikker.

## Hvad er kontekstengineering?

For AI-agenter er kontekst det, der driver planlægningen af en AI-agents handlinger. Kontekstengineering er praksissen med at sikre, at AI-agenten har den rette information til at fuldføre næste trin i opgaven. Kontekstvinduet er begrænset i størrelse, så som agentudviklere skal vi bygge systemer og processer til at håndtere tilføjelse, fjernelse og kondensering af information i kontekstvinduet.

### Promptengineering vs kontekstengineering

Promptengineering fokuserer på et enkelt sæt statiske instruktioner for effektivt at guide AI-agenter med et regelsæt. Kontekstengineering handler om, hvordan man håndterer et dynamisk informationssæt, inklusive den indledende prompt, for at sikre, at AI-agenten har det, den behøver over tid. Hovedideen i kontekstengineering er at gøre denne proces gentagelig og pålidelig.

### Typer af kontekst

[![Typer af kontekst](../../../translated_images/da/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Det er vigtigt at huske, at kontekst ikke kun er én ting. Den information, som AI-agenten behøver, kan komme fra mange forskellige kilder, og det er op til os at sikre, at agenten har adgang til disse kilder:

De typer kontekst, som en AI-agent måske skal håndtere, inkluderer:

• **Instruktioner:** Disse svarer til agentens "regler" – prompts, systembeskeder, few-shot eksempler (der viser AI’en, hvordan noget gøres) og beskrivelser af værktøjer, den kan bruge. Her kombineres fokus fra promptengineering med kontekstengineering.

• **Viden:** Dette dækker fakta, information hentet fra databaser eller langtidshukommelse, som agenten har opbygget. Dette inkluderer integration af et Retrieval Augmented Generation (RAG) system, hvis agenten skal have adgang til forskellige vidensdatabaser.

• **Værktøjer:** Disse er definitioner af eksterne funktioner, API’er og MCP-servere, som agenten kan kalde på, sammen med feedback'et (resultater) den får ved at bruge dem.

• **Samtalehistorik:** Den igangværende dialog med en bruger. Over tid bliver disse samtaler længere og mere komplekse, hvilket betyder, at de fylder i kontekstvinduet.

• **Brugerpræferencer:** Information lært om en brugers ønsker eller aversioner over tid. Disse kan gemmes og hentes frem, når nøglebeslutninger skal træffes for at hjælpe brugeren.

## Strategier for effektiv kontekstengineering

### Planlægningsstrategier

[![Bedste praksis for kontekstengineering](../../../translated_images/da/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

God kontekstengineering starter med god planlægning. Her er en tilgang, der vil hjælpe dig i gang med at tænke på, hvordan du anvender konceptet kontekstengineering:

1. **Definér klare resultater** - Resultaterne af de opgaver, som AI-agenter skal løse, bør være klart definerede. Besvar spørgsmålet – "Hvordan vil verden se ud, når AI-agenten er færdig med sin opgave?" Med andre ord, hvilken ændring, information eller respons skal brugeren have efter samspillet med AI-agenten.
2. **Kortlæg konteksten** - Når du har defineret AI-agentens resultater, skal du besvare spørgsmålet "Hvilken information skal AI-agenten bruge for at fuldføre denne opgave?". På den måde kan du begynde at kortlægge, hvor denne information kan findes.
3. **Opret kontekstpipelines** - Nu hvor du ved, hvor informationen er, skal du svare på spørgsmålet "Hvordan får agenten adgang til denne information?". Dette kan gøres på flere måder, inklusiv RAG, brug af MCP-servere og andre værktøjer.

### Praktiske strategier

Planlægning er vigtig, men når informationen begynder at flyde ind i agentens kontekstvindue, skal vi have praktiske strategier til at håndtere den:

#### Håndtering af kontekst

Selvom noget information automatisk bliver tilføjet til kontekstvinduet, handler kontekstengineering også om en mere aktiv tilgang til denne information, som kan ske gennem nogle få strategier:

 1. **Agentens notesblok**
 Dette giver AI-agenten mulighed for at tage noter om relevant information om de aktuelle opgaver og brugerinteraktioner under en enkelt session. Dette bør findes uden for kontekstvinduet i en fil eller runtime-objekt, som agenten senere kan hente under sessionen, hvis nødvendigt.

 2. **Hukommelser**
 Notesblokke er gode til at håndtere information uden for kontekstvinduet i en enkelt session. Hukommelser gør det muligt for agenter at gemme og hente relevant information på tværs af flere sessioner. Dette kan inkludere opsummeringer, brugerpræferencer og feedback til forbedringer i fremtiden.

 3. **Komprimering af kontekst**
  Når kontekstvinduet vokser og nærmer sig sin grænse, kan teknikker som opsummering og trimning bruges. Dette inkluderer enten kun at bevare den mest relevante information eller fjerne ældre beskeder.
  
 4. **Multi-agent systemer**
  Udvikling af multi-agent systemer er en form for kontekstengineering, fordi hver agent har sit eget kontekstvindue. Hvordan denne kontekst deles og overføres til forskellige agenter er et andet aspekt at planlægge, når man bygger disse systemer.
  
 5. **Sandbox-miljøer**
  Hvis en agent skal køre kode eller behandle store mængder information i et dokument, kan det tage mange tokens at behandle resultaterne. I stedet for at gemme det hele i kontekstvinduet, kan agenten bruge et sandbox-miljø, der kan køre denne kode og kun læse resultaterne og anden relevant information.
  
 6. **Runtime state-objekter**
   Dette sker ved at skabe informationsbeholdere til at håndtere situationer, hvor agenten skal have adgang til bestemt information. For en kompleks opgave gør dette det muligt for agenten at gemme resultaterne af hver delopgave trin for trin, så konteksten forbliver knyttet kun til den specifikke delopgave.

#### Inspektion af kontekst

Når du har anvendt en af disse strategier, er det værd at tjekke, hvad det næste modelkald faktisk modtog. Et brugbart debugging-spørgsmål er:

> Indlæste agenten for meget kontekst, forkert kontekst eller manglede den kontekst, den havde brug for?

Du behøver ikke logge rå prompts, værktøjsuddata eller hukommelsesindhold for at besvare det spørgsmål. I produktion foretrækkes små kontekstsinspektionsrecords, der fanger antal, id'er, hashes og politiklabels:

- **Udvælgelse:** Spor, hvor mange kandidatstykker, værktøjer eller hukommelser der blev overvejet, hvor mange der blev valgt, og hvilken regel eller score der fik de andre til at blive filtreret fra.
- **Komprimering:** Registrér kildeområdet eller spor-id, opsummerings-id, et estimeret tokenantal før og efter komprimering, og om råt indhold blev udelukket fra næste kald.
- **Isolering:** Notér hvilken delopgave, der blev kørt i en separat agent, session eller sandbox, hvilken afgrænset opsummering der blev returneret, og om stort værktøjsoutput blev holdt uden for forælderagentens kontekst.
- **Hukommelse og RAG:** Gem dokument-id'er for hentning, hukommelses-id'er, score, valgte id'er og status for redigering i stedet for fuld hentet tekst.
- **Sikkerhed og privatliv:** Foretræk hashes, id'er, tokenbuckets og politiklabels fremfor sensitiv prompttekst, værktøjsargumenter, værktøjsresultater eller brugerhukommelsesindhold.

Målet er ikke at beholde mere kontekst. Det er at efterlade nok beviser til, at en udvikler kan se, hvilken kontekststrategi der blev brugt, og om det ændrede næste modelkald på den tilsigtede måde.

### Eksempel på kontekstengineering

Lad os sige, at vi vil have en AI-agent til at **"Booke mig en rejse til Paris."**

• En simpel agent, der kun bruger promptengineering, ville måske bare svare: **"Okay, hvornår vil du gerne tage til Paris?**". Den behandlede kun dit direkte spørgsmål på det tidspunkt, brugeren stillede det.

• En agent, der bruger de gennemgåede strategier for kontekstengineering, ville gøre meget mere. Før den overhovedet svarer, kan dens system fx:

  ◦ **Tjekke din kalender** for ledige datoer (henter realtidsdata).

 ◦ **Huske tidligere rejsepræferencer** (fra langtidshukommelse) som dit foretrukne flyselskab, budget eller om du foretrækker direkte fly.

 ◦ **Identificere tilgængelige værktøjer** til fly- og hotelbooking.

- Derefter kunne et eksempel på svar være:  "Hej [Dit navn]! Jeg kan se, du er ledig den første uge i oktober. Skal jeg kigge efter direkte fly til Paris med [Foretrukne flyselskab] inden for dit sædvanlige budget på [Budget]?". Dette rigere, kontekstbevidste svar viser kontekstengineeringens styrke.

## Almindelige kontekstfejl

### Kontekstforgiftning

**Hvad det er:** Når en hallucination (falsk information genereret af LLM’en) eller en fejl kommer ind i konteksten og gentagne gange refereres, så agenten forfølger umulige mål eller udvikler nonsens-strategier.

**Hvad man gør:** Implementer **kontekstvalidering** og **kvarantæne**. Valider information, inden den tilføjes til langtidshukommelsen. Hvis potentiel forgiftning opdages, start nye konteksttråde for at forhindre spredning af den dårlige information.

**Eksempel på rejsebooking:** Din agent hallucinerer en **direkte flyvning fra en lille lokal lufthavn til en fjern international by**, som faktisk ikke tilbyder internationale flyvninger. Denne ikke-egentlige flyvningsdetalje bliver gemt i konteksten. Senere, når du beder agenten om at booke, prøver den konstant at finde billetter til denne umulige rute, hvilket fører til gentagne fejl.

**Løsning:** Implementer et trin, der **validerer flyvningens eksistens og ruter med en realtids-API** _før_ flydetaljen tilføjes agentens arbejds-kontekst. Hvis valideringen fejler, bliver den fejlagtige information "kvarantæneret" og ikke brugt yderligere.

### Kontekstdistraktion

**Hvad det er:** Når konteksten bliver så stor, at modellen fokuserer for meget på den ophobede historie i stedet for at bruge det, den lærte under træningen, hvilket fører til gentagende eller ikke-hjælpsomme handlinger. Modeller kan begynde at lave fejl, selv før kontekstvinduet er fyldt.

**Hvad man gør:** Brug **kontekstsammenfatning**. Komprimer periodisk den ophobede information til kortere opsummeringer, som bevarer vigtige detaljer og fjerner overflødig historik. Dette hjælper med at "nulstille" fokus.

**Eksempel på rejsebooking:** Du har i lang tid diskuteret forskellige drømmerejsemål, inklusive en detaljeret genfortælling af din backpacking-tur for to år siden. Når du endelig beder om at **"finde mig en billig flyrejse til næste måned"**, bliver agenten fanget i de gamle, irrelevante detaljer og bliver ved med at spørge ind til dit backpackutstyr eller tidligere rejseplaner, og overser din aktuelle forespørgsel.

**Løsning:** Efter et vist antal interaktioner eller når konteksten bliver for stor, bør agenten **opsummere de seneste og mest relevante dele af samtalen** – med fokus på dine nuværende rejsedatoer og destination – og bruge denne kondenserede opsummering til næste LLM-kald, mens den mindre relevante historik afvises.

### Kontekstforvirring

**Hvad det er:** Når unødvendig kontekst, ofte i form af for mange tilgængelige værktøjer, får modellen til at generere dårlige svar eller kalde irrelevante værktøjer. Mindre modeller er særligt sårbare over for dette.

**Hvad man gør:** Implementer **værktøjsloadout-styring** ved brug af RAG-teknikker. Gem værktøjsbeskrivelser i en vektordatabase og vælg _kun_ de mest relevante værktøjer til hver specifik opgave. Forskning viser, at begrænse værktøjsvalg til under 30 er optimalt.

**Eksempel på rejsebooking:** Din agent har adgang til dusinvis af værktøjer: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` osv. Du spørger, **"Hvad er den bedste måde at komme rundt i Paris på?"** På grund af det store antal værktøjer bliver agenten forvirret og forsøger at kalde `book_flight` _inden for_ Paris eller `rent_car`, selvom du foretrækker offentlig transport, fordi værktøjsbeskrivelserne kan overlappe, eller den simpelthen ikke kan afgøre det bedste værktøj.

**Løsning:** Brug **RAG over værktøjsbeskrivelser**. Når du spørger om at komme rundt i Paris, henter systemet dynamisk _kun_ de mest relevante værktøjer som `rent_car` eller `public_transport_info` baseret på din forespørgsel, og præsenterer et fokuseret "loadout" af værktøjer til LLM’en.

### Kontekstkonflikt

**Hvad det er:** Når modstridende information findes inden for konteksten, hvilket fører til inkonsistent ræsonnering eller dårlige endelige svar. Dette sker ofte, når information ankommer i etaper, og tidlige, forkerte antagelser stadig er i konteksten.

**Hvad man gør:** Brug **kontekstbeskæring** og **aflastning**. Beskæring betyder at fjerne forældet eller modstridende information, efterhånden som nye detaljer kommer til. Aflastning giver modellen en separat "notesblok"-arbejdsplads til at behandle information uden at gøre hovedkonteksten rodet.


**Eksempel på rejsebookning:** Du fortæller oprindeligt din agent, **"Jeg vil flyve økonomiklasse."** Senere i samtalen ændrer du mening og siger, **"Faktisk, for denne tur, lad os tage business class."** Hvis begge instruktioner forbliver i konteksten, kan agenten modtage modstridende søgeresultater eller blive forvirret om, hvilken præference der skal prioriteres.

**Løsning:** Implementer **kontekstbeskæring**. Når en ny instruktion strider imod en gammel, fjernes den ældre instruktion eller overskrives eksplicit i konteksten. Alternativt kan agenten bruge en **kladdeblok** til at forene modstridende præferencer, inden den træffer beslutning, hvilket sikrer, at kun den endelige, konsistente instruktion styrer dens handlinger.

## Har du flere spørgsmål om konteksteknik?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.
## Forrige lektion

[Agentiske Protokoller](../11-agentic-protocols/README.md)

## Næste lektion

[Hukommelse til AI-agenter](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->