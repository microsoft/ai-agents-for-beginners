# Kontekst­ingeniør­arbeid for AI-agenter

[![Kontekst­ingeniør­arbeid](../../../translated_images/no/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klikk på bildet over for å se video av denne leksjonen)_

Å forstå kompleksiteten i applikasjonen du bygger en AI-agent for er viktig for å lage en pålitelig en. Vi må bygge AI-agenter som effektivt håndterer informasjon for å imøtekomme komplekse behov utover prompt­ingeniør­arbeid.

I denne leksjonen ser vi på hva kontekst­ingeniør­arbeid er og dens rolle i å bygge AI-agenter.

## Introduksjon

Denne leksjonen vil dekke:

• **Hva kontekst­ingeniør­arbeid er** og hvorfor det er forskjellig fra prompt­ingeniør­arbeid.

• **Strategier for effektivt kontekst­ingeniør­arbeid**, inkludert hvordan skrive, velge, komprimere og isolere informasjon.

• **Vanlige kontekst­sfeil** som kan velte AI-agenten din og hvordan fikse dem.

## Læringsmål

Etter å ha fullført denne leksjonen vil du forstå hvordan du:

• **Definerer kontekst­ingeniør­arbeid** og skiller det fra prompt­ingeniør­arbeid.

• **Identifiserer de viktigste komponentene i kontekst** i applikasjoner med store språkmodeller (LLM).

• **Bruker strategier for å skrive, velge, komprimere og isolere kontekst** for å forbedre agentens ytelse.

• **Gjenkjenner vanlige kontekst­sfeil** som forgiftning, distraksjon, forvirring og konflikt, og implementerer tiltak.

## Hva er kontekst­ingeniør­arbeid?

For AI-agenter er kontekst det som driver planleggingen av agentens handlinger. Kontekst­ingeniør­arbeid handler om å sørge for at AI-agenten har riktig informasjon for å fullføre neste steg i oppgaven. Kontekstvinduet har begrenset størrelse, så som agentbyggere må vi lage systemer og prosesser for å styre å legge til, fjerne og kondensere informasjon i kontekstvinduet.

### Prompt­ingeniør­arbeid vs kontekst­ingeniør­arbeid

Prompt­ingeniør­arbeid fokuserer på et enkelt sett med statiske instruksjoner for effektivt å styre AI-agentene med et sett regler. Kontekst­ingeniør­arbeid handler om å håndtere et dynamisk sett med informasjon, inkludert den initielle prompten, for å sikre at AI-agenten har det den trenger over tid. Hovedideen med kontekst­ingeniør­arbeid er å gjøre denne prosessen gjentakbar og pålitelig.

### Typer kontekst

[![Typer kontekst](../../../translated_images/no/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Det er viktig å huske at kontekst ikke er bare én ting. Informasjonen AI-agenten trenger kan komme fra mange forskjellige kilder, og det er opp til oss å sikre at agenten har tilgang til disse kildene:

Typene kontekst en AI-agent kan trenge å håndtere inkluderer:

• **Instruksjoner:** Dette er som agentens "regler" – prompts, systemmeldinger, få-eksempler (few-shot) (som viser AI hvordan noe skal gjøres), og beskrivelser av verktøy den kan bruke. Her kombineres fokusene på prompt­ingeniør­arbeid og kontekst­ingeniør­arbeid.

• **Kunnskap:** Dekker fakta, informasjon hentet fra databaser, eller langsiktige minner agenten har akkumulert. Dette inkluderer å integrere et Retrieval Augmented Generation (RAG) system hvis agenten trenger tilgang til ulike kunnskaps­lager og databaser.

• **Verktøy:** Definisjonene av eksterne funksjoner, API-er og MCP-servere agenten kan kalle, sammen med tilbakemeldingen (resultatene) den får fra å bruke dem.

• **Samtale­historikk:** Den pågående dialogen med en bruker. Over tid blir disse samtalene lengre og mer komplekse, noe som tar opp plass i kontekstvinduet.

• **Bruker­preferanser:** Informasjon lært om en brukers liker eller misliker over tid. Disse kan lagres og hentes frem ved viktige beslutninger for å hjelpe brukeren.

## Strategier for effektivt kontekst­ingeniør­arbeid

### Planleggings­strategier

[![Beste praksis for kontekst­ingeniør­arbeid](../../../translated_images/no/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Godt kontekst­ingeniør­arbeid starter med god planlegging. Her er en tilnærming som vil hjelpe deg med å begynne å tenke på hvordan du bruker konseptet kontekst­ingeniør­arbeid:

1. **Definer klare resultater** – Resultatene av oppgavene AI-agentene skal utføre bør være klart definerte. Svar på spørsmålet – "Hvordan ser verden ut når AI-agenten er ferdig med oppgaven?" Med andre ord, hvilken endring, informasjon eller respons bør brukeren ha etter samhandling med AI-agenten.

2. **Kartlegg konteksten** – Når du har definert AI-agentens resultater, må du svare på spørsmålet "Hvilken informasjon trenger AI-agenten for å fullføre denne oppgaven?". Slik kan du begynne å kartlegge hvor informasjonen kan finnes.

3. **Lag kontekst­rør­ledninger** – Nå som du vet hvor informasjonen ligger, må du svare på spørsmålet "Hvordan får agenten denne informasjonen?". Dette kan gjøres på ulike måter, inkludert RAG, bruk av MCP-servere og andre verktøy.

### Praktiske strategier

Planlegging er viktig, men når informasjonen begynner å flyte inn i agentens kontekstvindu, trenger vi praktiske strategier for å håndtere det:

#### Håndtering av kontekst

Mens noe informasjon legges til kontekstvinduet automatisk, handler kontekst­ingeniør­arbeid om å ta en mer aktiv rolle med denne informasjonen, noe som kan gjøres med noen strategier:

 1. **Agentens notatblokk**  
 Dette gir en AI-agent mulighet til å ta notater om relevant informasjon om gjeldende oppgaver og brukerinteraksjoner under en enkelt økt. Dette bør eksistere utenfor kontekstvinduet, f.eks. i en fil eller et runtime-objekt som agenten kan hente senere i denne økten om nødvendig.

 2. **Minner**  
 Notatblokker er gode for å håndtere informasjon utenfor kontekstvinduet i en enkelt økt. Minner gjør det mulig for agenter å lagre og hente relevant informasjon på tvers av flere økter. Dette kan inkludere oppsummeringer, brukerpreferanser og tilbakemeldinger for forbedringer i fremtiden.

 3. **Kompresjon av kontekst**  
 Når kontekstvinduet vokser og nærmer seg sin grense, kan teknikker som oppsummering og trimming brukes. Dette inkluderer enten å beholde kun den mest relevante informasjonen eller fjerne eldre meldinger.
  
 4. **Multi-agent systemer**  
 Utvikling av multi-agent systemer er en form for kontekst­ingeniør­arbeid fordi hver agent har sitt eget kontekstvindu. Hvordan den konteksten deles og overføres til forskjellige agenter er noe annet å planlegge når man bygger disse systemene.
  
 5. **Sandkasse­miljøer**  
 Hvis en agent trenger å kjøre kode eller prosessere store mengder informasjon i et dokument, kan dette bruke mange tokens for å behandle resultatene. I stedet for å lagre alt i kontekstvinduet, kan agenten bruke et sandkasse­miljø som kjører koden og kun leser resultatene og relevant informasjon.
  
 6. **Runtime-tilstands­objekter**  
 Dette skjer ved å lage informasjonssamlinger for å håndtere situasjoner når agenten trenger tilgang til bestemt informasjon. For en kompleks oppgave kan dette tillate agenten å lagre resultatene fra hvert delsteg etter hvert, slik at konteksten forblir knyttet bare til den spesifikke deloppgaven.

#### Inspeksjon av kontekst

Etter at du har brukt en av disse strategiene, er det verdt å sjekke hva neste modell-kall faktisk mottok. Et nyttig feilsøkingsspørsmål er:

> Lastet agenten for mye kontekst, feil kontekst, eller manglet den kontekst den trengte?

Du trenger ikke logge råprompter, verktøyutdata eller minneinnhold for å svare på dette spørsmålet. I produksjon foretrekk små kontekstinspeksjons­logger som fanger opptelling, ID-er, hasher og policy­etiketter:

- **Utvalg:** Følg med på hvor mange kandidat­deler, verktøy eller minner som ble vurdert, hvor mange som ble valgt, og hvilken regel eller poengsum som førte til at andre ble filtrert bort.

- **Kompresjon:** Logg kilde­område eller sporings-ID, oppsummerings-ID, estimert token­tall før og etter kompresjon, og om råinnholdet ble ekskludert fra neste kall.

- **Isolering:** Noter hvilken deloppgave som kjørte i en separat agent, økt eller sandkasse, hvilken begrenset oppsummering som ble returnert, og om store verktøy­resultater forble utenfor hovedagentens kontekst.

- **Minne og RAG:** Lagre ID-er for hentede dokumenter, minne-ID-er, poeng, valgte ID-er, og redigeringsstatus i stedet for full hentet tekst.

- **Sikkerhet og personvern:** Foretrekk hasher, ID-er, token-hinkesystemer og policy-etiketter fremfor sensitiv prompt-tekst, verktøy-argumenter, verktøy-resultater eller bruker-minneinnhold.

Målet er ikke å beholde mer kontekst, men å legge igjen nok bevis slik at en utvikler kan se hvilken kontekst­strategi som kjørte og om den endret neste modellkall på tiltenkt måte.

### Eksempel på kontekst­ingeniør­arbeid

La oss si vi ønsker at en AI-agent skal **"Bestille en tur til Paris for meg."**

• En enkel agent som bare bruker prompt­ingeniør­arbeid kan bare svare: **"Ok, når vil du reise til Paris?"** Den behandlet bare ditt direkte spørsmål da du spurte.

• En agent som bruker de dekkede kontekst­ingeniør­strategiene vil gjøre mye mer. Før den i det hele tatt svarer, kan systemet for eksempel:

  ◦ **Sjekke kalenderen din** for ledige datoer (hente sanntidsdata).

 ◦ **Hente frem tidligere reisepreferanser** (fra langtidsminne) som foretrukket flyselskap, budsjett eller om du foretrekker direkteflyvninger.

 ◦ **Identifisere tilgjengelige verktøy** for fly- og hotell­bestilling.

- Så kan et eksempel­svar være: "Hei [Ditt navn]! Jeg ser du er ledig første uke i oktober. Skal jeg se etter direktefly til Paris på [Foretrukket flyselskap] innen ditt vanlige budsjett på [Budsjett]?" Dette rikere, kontekst­bevisste svaret viser kraften i kontekst­ingeniør­arbeid.

## Vanlige kontekst­feil

### Forgiftning av kontekst

**Hva det er:** Når en hallusinasjon (feilinformasjon generert av LLM) eller en feil kommer inn i konteksten og gjentas, slik at agenten forsøker å nå umulige mål eller utvikler meningsløse strategier.

**Hva du bør gjøre:** Implementer **kontekst­validering** og **karantene**. Valider informasjon før den legges i langtidsminne. Ved potensiell forgiftning start nye kontekst­tråder for å forhindre spredning av feilinformasjonen.

**Eksempel på reisebestilling:** Agenten din hallusinerer en **direkteflyvning fra en liten lokal flyplass til en fjern internasjonal by** som faktisk ikke har internasjonale flyvninger. Denne ikke-eksisterende flydetaljen lagres i konteksten. Senere, når du ber agenten bestille, prøver den stadig å finne billetter for denne umulige ruten, noe som fører til gjentatte feil.

**Løsning:** Implementer et steg som **validerer at flyet finnes og rutene med en API i sanntid** _før_ flydetaljen legges til agentens arbeidskontekst. Hvis valideringen feiler, blir feilinformasjonen "karantenesatt" og ikke brukt videre.

### Distraksjon av kontekst

**Hva det er:** Når konteksten blir så stor at modellen fokuserer for mye på den akkumulerte historien i stedet for det den lærte under trening, noe som fører til repetitiv eller ubrukelig atferd. Modeller kan begynne å gjøre feil før kontekstvinduet er fullt.

**Hva du bør gjøre:** Bruk **kontekst­oppsummering**. Komprimer periodisk akkumulert informasjon til kortere oppsummeringer, behold viktige detaljer og fjern overflødig historie. Dette hjelper å "tilbakestille" fokuset.

**Eksempel på reisebestilling:** Du har diskutert ulike drømmereisedestinasjoner lenge, inkludert en detaljert fortelling om ryggsekktur for to år siden. Når du endelig ber om å **"finne en billig flybillett for neste måned"**, blir agenten hængende fast i gamle, irrelevante detaljer og spør stadig om ryggsekkutstyr eller tidligere reiseruter, mens den overser ditt nåværende ønske.

**Løsning:** Etter et visst antall runder eller når konteksten vokser for stor, bør agenten **oppsummere de mest nylige og relevante delene av samtalen** – fokusere på dine nåværende reisedatoer og destinasjon – og bruke denne kondenserte oppsummeringen for neste LLM-kall, mens den kasserer mindre relevante historiske deler.

### Forvirring av kontekst

**Hva det er:** Når unødvendig kontekst, ofte i form av for mange tilgjengelige verktøy, får modellen til å lage dårlige svar eller kalle irrelevante verktøy. Mindre modeller er spesielt utsatt for dette.

**Hva du bør gjøre:** Implementer **verktøy­last­styring** med RAG-teknikker. Lagre verktøy­beskrivelser i en vektor­database og velg _kun_ de mest relevante verktøyene for hver oppgave. Forskning viser begrensning til færre enn 30 verktøy.

**Eksempel på reisebestilling:** Agenten din har tilgang til dusinvis av verktøy: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, osv. Du spør, **"Hva er den beste måten å komme seg rundt i Paris?"** På grunn av det store antallet verktøy, blir agenten forvirret og forsøker å kalle `book_flight` _innenfor_ Paris, eller `rent_car` selv om du foretrekker kollektivtransport, siden verktøy­beskrivelsene kan overlappe eller den ikke klarer å avgjøre det beste.

**Løsning:** Bruk **RAG over verktøy­beskrivelser**. Når du spør om å komme deg rundt i Paris, henter systemet dynamisk _kun_ de mest relevante verktøyene som `rent_car` eller `public_transport_info` basert på spørsmålet ditt, og presenterer en fokusert "last" av verktøy til LLM.

### Konflikt i kontekst

**Hva det er:** Når motstridende informasjon finnes i konteksten, noe som fører til inkonsekvent resonnement eller dårlige sluttsvar. Dette skjer ofte når informasjon kommer i etapper, og tidlige feilaktige antakelser fortsatt ligger i konteksten.

**Hva du bør gjøre:** Bruk **kontekst­beskjæring** og **utlasting**. Beskjæring betyr å fjerne foreldet eller motstridende informasjon når nye detaljer kommer inn. Utlasting gir modellen et separat "notatblokk"-arbeidsområde for å behandle informasjon uten å rote til hovedkonteksten.
**Reisebestillingseksempel:** Du forteller agenten din først, **"Jeg vil fly økonomiklasse."** Senere i samtalen ombestemmer du deg og sier, **"Egentlig, la oss ta businessklasse på denne turen."** Hvis begge instruksjonene forblir i konteksten, kan agenten motta motstridende søkeresultater eller bli forvirret om hvilken preferanse som skal prioriteres.

**Løsning:** Implementer **kontekstrensing**. Når en ny instruksjon motsier en gammel, fjernes den eldre instruksjonen eller overstyres eksplisitt i konteksten. Alternativt kan agenten bruke en **scratchpad** for å forene motstridende preferanser før den bestemmer seg, og sikre at bare den endelige, konsistente instruksjonen styrer handlingene.

## Har du flere spørsmål om kontekstteknikk?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre elever, delta på kontortimer og få svar på spørsmål om AI-agenter.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->