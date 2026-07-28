# Kontekstingeniørkunst for AI-agenter

[![Kontekstingeniørkunst](../../../translated_images/no/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klikk på bildet over for å se video av denne leksjonen)_

Å forstå kompleksiteten i applikasjonen du bygger en AI-agent for, er viktig for å lage en pålitelig en. Vi må bygge AI-agenter som effektivt håndterer informasjon for å dekke komplekse behov utover prompt-ingeniørkunst.

I denne leksjonen vil vi se på hva kontekstingeniørkunst er og dens rolle i bygging av AI-agenter.

## Innledning

Denne leksjonen vil dekke:

• **Hva kontekstingeniørkunst er** og hvorfor det er forskjellig fra prompt-ingeniørkunst.

• **Strategier for effektiv kontekstingeniørkunst**, inkludert hvordan man skriver, velger, komprimerer og isolerer informasjon.

• **Vanlige kontekstfeil** som kan støte din AI-agent og hvordan fikse dem.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du forstå hvordan å:

• **Definere kontekstingeniørkunst** og skille det fra prompt-ingeniørkunst.

• **Identifisere nøkkelkomponentene i kontekst** i applikasjoner med store språkmodeller (LLM).

• **Anvende strategier for å skrive, velge, komprimere og isolere kontekst** for å forbedre agentens ytelse.

• **Gjenkjenne vanlige kontekstfeil** som forgiftning, distraksjon, forvirring, og konflikt, og implementere avbøtende teknikker.

## Hva er kontekstingeniørkunst?

For AI-agenter er kontekst det som driver planleggingen av en AI-agent for å utføre bestemte handlinger. Kontekstingeniørkunst er praksisen med å sikre at AI-agenten har riktig informasjon for å fullføre neste trinn i oppgaven. Kontekstvinduet er begrenset i størrelse, så som agentbyggere må vi lage systemer og prosesser for å håndtere å legge til, fjerne og kondensere informasjonen i kontekstvinduet.

### Prompt-ingeniørkunst vs kontekstingeniørkunst

Prompt-ingeniørkunst fokuserer på et enkelt sett med statiske instruksjoner for å effektivt veilede AI-agentene med et sett regler. Kontekstingeniørkunst handler om hvordan man håndterer et dynamisk sett med informasjon, inkludert den innledende prompten, for å sikre at AI-agenten har det den trenger over tid. Hovedideen rundt kontekstingeniørkunst er å gjøre denne prosessen repeterbar og pålitelig.

### Typer av kontekst

[![Typer av kontekst](../../../translated_images/no/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Det er viktig å huske at kontekst ikke er bare én ting. Informasjonen som AI-agenten trenger kan komme fra en rekke forskjellige kilder, og det er opp til oss å sikre at agenten har tilgang til disse kildene:

Typene kontekst en AI-agent kan trenge å håndtere inkluderer:

• **Instruksjoner:** Disse er som agentens "regler" – prompts, systemmeldinger, få-skudd-eksempler (som viser AI hvordan man gjør noe) og beskrivelser av verktøy den kan bruke. Dette er der fokuset på prompt-ingeniørkunst kombineres med kontekstingeniørkunst.

• **Kunnskap:** Dette dekker fakta, informasjon hentet fra databaser, eller langtidsminner agenten har akkumulert. Dette inkluderer integrering av en Retrieval Augmented Generation (RAG)-system hvis en agent trenger tilgang til forskjellige kunnskapslager og databaser.

• **Verktøy:** Dette er definisjoner av eksterne funksjoner, API-er og MCP-servere som agenten kan kalle på, sammen med tilbakemeldingene (resultatene) den får fra å bruke dem.

• **Samtalehistorikk:** Den pågående dialogen med en bruker. Over tid blir disse samtalene lengre og mer komplekse, som betyr at de tar opp plass i kontekstvinduet.

• **Brukerpreferanser:** Informasjon som læres om en brukers liker eller misliker over tid. Disse kan lagres og hentes frem ved viktige beslutninger for å hjelpe brukeren.

## Strategier for effektiv kontekstingeniørkunst

### Planleggingsstrategier

[![Beste praksis for kontekstingeniørkunst](../../../translated_images/no/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

God kontekstingeniørkunst starter med god planlegging. Her er en tilnærming som vil hjelpe deg å begynne å tenke på hvordan du kan anvende konseptet kontekstingeniørkunst:

1. **Definer klare resultater** - Resultatene av oppgavene AI-agentene får tildelt bør være klart definerte. Svar på spørsmålet - "Hvordan vil verden se ut når AI-agenten er ferdig med sin oppgave?" Med andre ord, hvilken endring, informasjon eller respons bør brukeren ha etter å ha interagert med AI-agenten.
2. **Kartlegg konteksten** - Når du har definert resultatene av AI-agenten, må du svare på spørsmålet "Hvilken informasjon trenger AI-agenten for å fullføre denne oppgaven?". På denne måten kan du begynne å kartlegge hvor informasjonen kan finnes.
3. **Lag kontekstpipelines** - Nå som du vet hvor informasjonen er, må du svare på spørsmålet "Hvordan vil agenten få tak i denne informasjonen?". Dette kan gjøres på flere måter, inkludert RAG, bruk av MCP-servere og andre verktøy.

### Praktiske strategier

Planlegging er viktig, men når informasjon begynner å strømme inn i agentens kontekstvindu, trenger vi praktiske strategier for å håndtere det:

#### Håndtering av kontekst

Selv om noe informasjon vil bli lagt til kontekstvinduet automatisk, handler kontekstingeniørkunst om å ta en mer aktiv rolle i denne informasjonen, noe som kan gjøres med noen få strategier:

 1. **Agentens notatblokk**
 Dette gir en AI-agent mulighet til å ta notater om relevant informasjon om nåværende oppgaver og brukerinteraksjoner i løpet av en enkelt økt. Dette bør eksistere utenfor kontekstvinduet i en fil eller runtime-objekt som agenten senere kan hente under denne økten hvis nødvendig.

 2. **Minner**
 Notatblokker er gode til å håndtere informasjon utenfor kontekstvinduet for en enkelt økt. Minner gjør det mulig for agenter å lagre og hente relevant informasjon på tvers av flere økter. Dette kan inkludere sammendrag, brukerpreferanser og tilbakemeldinger for forbedringer i fremtiden.

 3. **Kompressering av kontekst**
  Når kontekstvinduet vokser og nærmer seg sin grense, kan teknikker som oppsummering og beskjæring brukes. Dette inkluderer enten å beholde bare den mest relevante informasjonen eller fjerne eldre meldinger.
  
 4. **Systemer med flere agenter**
  Utvikling av multisystemer er en form for kontekstingeniørkunst fordi hver agent har sitt eget kontekstvindu. Hvordan det konteksten deles og overføres til ulike agenter er noe du også må planlegge når du bygger disse systemene.
  
 5. **Sandbox-miljøer**
  Hvis en agent trenger å kjøre kode eller behandle store mengder informasjon i et dokument, kan dette kreve et stort antall tokens for å behandle resultatene. I stedet for å ha alt dette lagret i kontekstvinduet, kan agenten bruke et sandbox-miljø som kan kjøre denne koden og bare lese resultatene og annen relevant informasjon.
  
 6. **Runtime-tilstandobjekter**
   Dette gjøres ved å lage containere med informasjon for å håndtere situasjoner hvor agenten trenger å ha tilgang til bestemt informasjon. For en kompleks oppgave gjør dette det mulig for agenten å lagre resultatene av hver deloppgave steg for steg, slik at konteksten forblir knyttet kun til den spesifikke deloppgaven.

#### Inspisere kontekst

Etter at du har anvendt en av disse strategiene, er det verdt å sjekke hva det neste modellkallet faktisk mottok. Et nyttig debugging-spørsmål er:

> Lastet agenten for mye kontekst, feil kontekst, eller manglet nødvendig kontekst?

Du trenger ikke logge rå prompts, verktøyutdata eller minneinnhold for å svare på det spørsmålet. I produksjon, foretrekk små inspeksjonslogger for kontekst som fanger tellinger, ID-er, hasher og policyetiketter:

- **Valg:** Spor hvor mange kandidatbiter, verktøy eller minner som ble vurdert, hvor mange som ble valgt, og hvilken regel eller poengsum som førte til at de andre ble fjernet.
- **Kompresjon:** Registrer kildeområde eller sporing-ID, sammendrags-ID, et estimat over tokenantall før og etter komprimering, og om råinnholdet ble ekskludert fra neste kall.
- **Isolasjon:** Noter hvilken deloppgave som kjørte i en separat agent, økt eller sandbox, hvilket begrenset sammendrag som ble returnert, og om store verktøyutdata holdt seg utenfor hovedagentens kontekst.
- **Minne og RAG:** Lagre hentingsdokument-ID-er, minne-ID-er, poeng, valgte ID-er og redigeringsstatus i stedet for full hentet tekst.
- **Sikkerhet og personvern:** Foretrekk hasher, ID-er, token-bøtter og policyetiketter framfor sensitiv prompttekst, verktøyargumenter, verktøyresultater eller brukerminneinnhold.

Målet er ikke å beholde mer kontekst. Det er å legge igjen nok bevis slik at en utvikler kan si hvilken kontekststrategi som kjørte og om det endret det neste modellkallet på ønsket måte.

### Eksempel på kontekstingeniørkunst

La oss si vi ønsker en AI-agent til å **"Bestille en tur til Paris for meg."**

• En enkel agent som bare bruker prompt-ingeniørkunst kan bare svare: **"Ok, når vil du reise til Paris?"** Den behandlet bare ditt direkte spørsmål på tidspunktet brukeren spurte.

• En agent som bruker kontekstingeniørstrategiene vi har gjennomgått, ville gjort mye mer. Før den i det hele tatt svarte, kunne systemet gjøre følgende:

  ◦ **Sjekke kalenderen din** for tilgjengelige datoer (hente sanntidsdata).

 ◦ **Huske tidligere reisepreferanser** (fra langtidsminnet) som ditt foretrukne flyselskap, budsjett, eller om du foretrekker direktefly.

 ◦ **Identifisere tilgjengelige verktøy** for fly- og hotellbestilling.

- Deretter kunne et eksempel på svar være:  "Hei [Ditt navn]! Jeg ser at du er ledig første uke i oktober. Skal jeg se etter direktefly til Paris med [Foretrukket flyselskap] innenfor ditt vanlige budsjett på [Budsjett]?" Denne rikere, kontekstbevisste responsen demonstrerer kraften i kontekstingeniørkunst.

## Vanlige kontekstfeil

### Kontekstforgiftning

**Hva det er:** Når en hallusinasjon (feilinformasjon generert av LLM) eller en feil kommer inn i konteksten og refereres til gjentatte ganger, noe som får agenten til å forfølge umulige mål eller utvikle meningsløse strategier.

**Hva man skal gjøre:** Implementer **kontekstvalidering** og **karantene**. Validér informasjon før den legges til langtidsminnet. Hvis potensiell forgiftning oppdages, start friske konteksttråder for å hindre at den dårlige informasjonen sprer seg.

**Eksempel på reisebestilling:** Agenten din hallusinerer en **direkteflyvning fra en liten lokal flyplass til en fjern internasjonal by** som faktisk ikke tilbyr internasjonale flyvninger. Denne ikke-eksisterende flydetaljen blir lagret i konteksten. Senere, når du ber agenten om å bestille, prøver den hele tiden å finne billetter til denne umulige ruten, noe som fører til gjentatte feil.

**Løsning:** Implementer et steg som **validerer flyvningens eksistens og ruter med en sanntids-API** _før_ flydetaljen legges til agentens arbeidskontekst. Hvis valideringen feiler, settes feilinformasjonen i "karantene" og brukes ikke videre.

### Kontekstdistraksjon

**Hva det er:** Når konteksten blir så stor at modellen fokuserer for mye på akkumulert historikk i stedet for å bruke det den lærte under treningen, noe som fører til repeterende eller unyttige handlinger. Modeller kan begynne å gjøre feil selv før kontekstvinduet er fullt.

**Hva man skal gjøre:** Bruk **kontekstsammendrag**. Komprimer periodisk akkumulert informasjon til kortere sammendrag, behold viktige detaljer mens du fjerner overflødig historikk. Dette hjelper til å "nullstille" fokuset.

**Eksempel på reisebestilling:** Du har diskutert forskjellige drømmereisemål lenge, inkludert en detaljert gjennomgang av din backpackingtur for to år siden. Når du endelig spør om "**finn meg en billig flyreise for neste måned**," blir agenten overveldet av de gamle, irrelevante detaljene og fortsetter å spørre om ryggsekken eller tidligere reiseruter, og overser din nåværende forespørsel.

**Løsning:** Etter et visst antall runder eller når konteksten blir for stor, bør agenten **sammendrage de siste og mest relevante delene av samtalen** – fokusert på dine nåværende reisedatoer og destinasjon – og bruke dette komprimerte sammendraget for neste LLM-kall, og forkaste den mindre relevante historiske samtalen.

### Konfunderende kontekst

**Hva det er:** Når unødvendig kontekst, ofte i form av for mange tilgjengelige verktøy, får modellen til å generere dårlige svar eller kalle irrelevante verktøy. Mindre modeller er særlig utsatt for dette.

**Hva man skal gjøre:** Implementer **verktøybelastningshåndtering** ved bruk av RAG-teknikker. Lagre verktøybeskrivelser i en vektordatabase og velg _kun_ de mest relevante verktøyene for hver spesifikke oppgave. Forskning viser at man bør begrense verktøyvalg til færre enn 30.

**Eksempel på reisebestilling:** Agenten din har tilgang til dusinvis av verktøy: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, osv. Du spør, **"Hva er den beste måten å komme seg rundt i Paris?"** På grunn av det store antallet verktøy blir agenten forvirret og prøver å kalle `book_flight` _innenfor_ Paris, eller `rent_car` selv om du foretrekker offentlig transport, fordi verktøybeskrivelsene kan overlappe eller den rett og slett ikke kan skille det beste.

**Løsning:** Bruk **RAG over verktøybeskrivelser**. Når du spør om hvordan du kommer deg rundt i Paris, henter systemet dynamisk _kun_ de mest relevante verktøyene som `rent_car` eller `public_transport_info` basert på forespørselen din, og presenterer en fokusert "belastning" av verktøy til LLM.

### Kontextkonflikt

**Hva det er:** Når motstridende informasjon finnes i konteksten, som fører til inkonsistent resonnement eller dårlige sluttresponser. Dette skjer ofte når informasjon kommer i etapper, og tidlige, feilaktige antakelser forblir i konteksten.

**Hva man skal gjøre:** Bruk **kontekstbeskjæring** og **avlastning**. Beskjæring betyr å fjerne utdatert eller motstridende informasjon etter hvert som nye detaljer kommer til. Avlastning gir modellen et separat "notatblokk"-arbeidsområde for å behandle informasjon uten å rote til hovedkonteksten.


**Reiseer booking eksempel:** Du forteller først agenten din, **"Jeg vil fly økonomiklasse."** Senere i samtalen ombestemmer du deg og sier, **"Egentlig, for denne turen, la oss gå for business class."** Hvis begge instruksjonene fortsatt er i konteksten, kan agenten få motstridende søkeresultater eller bli forvirret om hvilken preferanse som skal prioriteres.

**Løsning:** Implementer **kontekstbeskjæring**. Når en ny instruksjon motsier en gammel, fjernes den eldre instruksjonen eller overskrives eksplisitt i konteksten. Alternativt kan agenten bruke en **notatblokk** for å forene motstridende preferanser før avgjørelse, slik at bare den endelige, konsistente instruksjonen styrer handlingene dens.

## Har du flere spørsmål om kontekstengineering?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre elever, delta på kontortid og få spørsmål om AI-agenter besvart.
## Forrige leksjon

[Agentiske protokoller](../11-agentic-protocols/README.md)

## Neste leksjon

[Minne for AI-agenter](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->