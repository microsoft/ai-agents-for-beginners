[![Multi-agent design](../../../translated_images/no/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikk bildet ovenfor for å se videoen av denne leksjonen)_

# Designmønstre for multi-agent-systemer

Så snart du begynner å jobbe med et prosjekt som involverer flere agenter, må du vurdere designmønsteret for multi-agenter. Det kan imidlertid ikke være umiddelbart klart når du skal bytte til flere agenter og hva fordelene er.

## Introduksjon

I denne leksjonen ønsker vi å svare på følgende spørsmål:

- Hvilke scenarier er det hvor flere agenter er aktuelle?
- Hva er fordelene ved å bruke flere agenter i stedet for bare én enkelt agent som utfører flere oppgaver?
- Hva er byggesteinene for å implementere designmønsteret for flere agenter?
- Hvordan får vi oversikt over hvordan de flere agentene samhandler med hverandre?

## Læringsmål

Etter denne leksjonen bør du kunne:

- Identifisere scenarier der flere agenter er aktuelle
- Gjenkjenne fordelene ved å bruke flere agenter i stedet for en enkelt agent.
- Forstå byggesteinene for å implementere designmønsteret for flere agenter.

Hva er det større bildet?

*Multi-agenter er et designmønster som lar flere agenter samarbeide for å nå et felles mål*.

Dette mønsteret brukes mye innen ulike felt, inkludert robotikk, autonome systemer og distribuert databehandling.

## Scenarier der flere agenter er aktuelle

Så hvilke scenarier er et godt bruksområde for å bruke flere agenter? Svaret er at det finnes mange scenarier hvor det er fordelaktig å bruke flere agenter, spesielt i følgende tilfeller:

- **Store arbeidsmengder**: Store arbeidsmengder kan deles inn i mindre oppgaver og tildeles ulike agenter, noe som muliggjør parallell behandling og raskere fullføring. Et eksempel på dette er ved store databehandlingsoppgaver.
- **Komplekse oppgaver**: Komplekse oppgaver, som store arbeidsmengder, kan brytes ned i mindre deloppgaver og tildeles ulike agenter, der hver spesialiserer seg på en bestemt del av oppgaven. Et godt eksempel på dette er autonome kjøretøy hvor forskjellige agenter håndterer navigasjon, hindringsdeteksjon og kommunikasjon med andre kjøretøy.
- **Variert ekspertise**: Ulike agenter kan ha ulik ekspertise, slik at de kan håndtere forskjellige aspekter av en oppgave mer effektivt enn én enkelt agent. Et godt eksempel på dette er innen helsevesenet hvor agenter kan håndtere diagnostikk, behandlingsplaner og pasientovervåking.

## Fordeler ved å bruke flere agenter fremfor en enkelt agent

Et system med én enkelt agent kan fungere godt for enkle oppgaver, men for mer komplekse oppgaver kan bruk av flere agenter gi flere fordeler:

- **Spesialisering**: Hver agent kan være spesialisert for en bestemt oppgave. Manglende spesialisering i en enkelt agent betyr at du har en agent som kan gjøre alt, men som kan bli forvirret når den står overfor en kompleks oppgave. Den kan for eksempel ende opp med å gjøre en oppgave den ikke er best egnet for.
- **Skalerbarhet**: Det er enklere å skalere systemer ved å legge til flere agenter i stedet for å overbelaste en enkelt agent.
- **Feiltoleranse**: Hvis en agent feiler, kan andre fortsette å fungere, noe som sikrer systemets pålitelighet.

La oss ta et eksempel: la oss bestille en reise for en bruker. Et system med én enkelt agent måtte håndtere alle aspekter av reisebestillingsprosessen, fra å finne fly til å bestille hoteller og leiebiler. For å få dette til med én enkelt agent, måtte agenten ha verktøy for å håndtere alle disse oppgavene. Dette kunne føre til et komplekst og monolitisk system som er vanskelig å vedlikeholde og skalere. Et multi-agent-system, derimot, kunne ha forskjellige agenter som er spesialiserte på å finne fly, bestille hoteller og leiebiler. Dette ville gjøre systemet mer modularisert, lettere å vedlikeholde og skalerbart.

Sammenlign dette med et reisebyrå drevet som en familiedrevet butikk versus et reisebyrå drevet som en franchise. Den familiedrevne butikken ville ha en enkelt agent som håndterer alle aspekter av reisebestillingsprosessen, mens franchisen ville ha forskjellige agenter som håndterer ulike aspekter av prosessen.

## Byggesteiner for implementering av designmønsteret for flere agenter

Før du kan implementere designmønsteret for flere agenter, må du forstå byggesteinene som utgjør mønsteret.

La oss gjøre dette mer konkret ved igjen å se på eksempelet med å bestille en reise for en bruker. I dette tilfellet vil byggesteinene inkludere:

- **Agentkommunikasjon**: Agenter for å finne fly, bestille hoteller og leiebiler må kommunisere og dele informasjon om brukerens preferanser og begrensninger. Du må bestemme protokollene og metodene for denne kommunikasjonen. Det dette betyr konkret er at agenten for å finne fly må kommunisere med agenten for å bestille hoteller for å sikre at hotellet er booket for de samme datoene som flyet. Det betyr at agentene må dele informasjon om brukerens reisedatoer, hvilket innebærer at du må bestemme *hvilke agenter som deler informasjon og hvordan de deler informasjon*.
- **Koordineringsmekanismer**: Agentene må koordinere handlingene sine for å sikre at brukerens preferanser og begrensninger blir møtt. En brukerpreferanse kan være at de ønsker et hotell nær flyplassen, mens en begrensning kan være at leiebiler kun er tilgjengelige på flyplassen. Dette betyr at agenten som bestiller hotell må koordinere med agenten som bestiller leiebiler for å sikre at brukerens preferanser og begrensninger blir møtt. Dette betyr at du må bestemme *hvordan agentene koordinerer handlingene sine*.
- **Agentarkitektur**: Agentene må ha intern struktur for å ta beslutninger og lære av sine interaksjoner med brukeren. Dette betyr at agenten som finner fly må ha intern struktur for å ta beslutninger om hvilke fly som skal anbefales til brukeren. Dette betyr at du må bestemme *hvordan agentene tar beslutninger og lærer av sine interaksjoner med brukeren*. Eksempler på hvordan en agent lærer og forbedrer seg kan være at agenten som finner fly kan bruke en maskinlæringsmodell for å anbefale fly til brukeren basert på tidligere preferanser.
- **Synlighet i samspillet mellom agenter**: Du må ha innsikt i hvordan de flere agentene samhandler med hverandre. Dette betyr at du trenger verktøy og teknikker for å spore agentaktiviteter og interaksjoner. Dette kan være i form av logg- og overvåkingsverktøy, visualiseringsverktøy og ytelsesmetrikker.
- **Multi-agent-mønstre**: Det finnes forskjellige mønstre for å implementere multi-agent-systemer, slik som sentralisert, desentralisert og hybride arkitekturer. Du må bestemme hvilket mønster som passer best for ditt brukstilfelle.
- **Mennesket i sløyfen**: I de fleste tilfeller vil du ha et menneske i sløyfen, og du må instruere agentene om når de skal be om menneskelig inngripen. Dette kan være i form av at en bruker ber om et spesifikt hotell eller fly som agentene ikke har anbefalt, eller ber om bekreftelse før bestilling av et fly eller hotell.

## Synlighet i samspillet mellom agenter

Det er viktig at du har innsikt i hvordan de flere agentene samhandler med hverandre. Denne synligheten er essensiell for feilsøking, optimalisering og for å sikre systemets samlede effektivitet. For å oppnå dette trenger du verktøy og teknikker for å spore agentaktiviteter og interaksjoner. Dette kan være i form av logg- og overvåkingsverktøy, visualiseringsverktøy og ytelsesmetrikker.

For eksempel, i tilfellet med å bestille en reise for en bruker, kan du ha et dashbord som viser statusen til hver agent, brukerens preferanser og begrensninger, og interaksjonene mellom agentene. Dette dashbordet kan vise brukerens reisedatoer, flyene anbefalt av flyagenten, hotellene anbefalt av hotellagenten og leiebilene anbefalt av leiebilagenten. Dette vil gi deg en klar oversikt over hvordan agentene samhandler med hverandre og om brukerens preferanser og begrensninger blir oppfylt.

La oss se nærmere på hver av disse aspektene.

- **Logg- og overvåkingsverktøy**: Du bør ha logging for hver handling som tas av en agent. En loggoppføring kan lagre informasjon om hvilken agent som utførte handlingen, handlingen som ble utført, tidspunktet handlingen ble utført og utfallet av handlingen. Denne informasjonen kan så brukes til feilsøking, optimalisering og mer.
- **Visualiseringsverktøy**: Visualiseringsverktøy kan hjelpe deg å se interaksjonene mellom agenter på en mer intuitiv måte. For eksempel kan du ha en graf som viser informasjonsflyten mellom agentene. Dette kan hjelpe deg med å identifisere flaskehalser, ineffektiviteter og andre problemer i systemet.
- **Ytelsesmetrikker**: Ytelsesmetrikker kan hjelpe deg med å spore effektiviteten til multi-agent-systemet. For eksempel kan du spore tiden det tar å fullføre en oppgave, antall oppgaver fullført per tidsenhet, og nøyaktigheten av anbefalingene som agentene gir. Denne informasjonen kan hjelpe deg med å identifisere forbedringsområder og optimalisere systemet.

## Multi-agent-mønstre

La oss gå nærmere inn på noen konkrete mønstre vi kan bruke for å lage multi-agent-apper. Her er noen interessante mønstre verdt å vurdere:

### Gruppesamtale

Dette mønsteret er nyttig når du ønsker å lage en gruppechat-applikasjon hvor flere agenter kan kommunisere med hverandre. Typiske bruksområder for dette mønsteret inkluderer team-samarbeid, kundestøtte og sosiale nettverk.

I dette mønsteret representerer hver agent en bruker i gruppechatten, og meldinger utveksles mellom agenter ved bruk av en meldingsprotokoll. Agentene kan sende meldinger til gruppechatten, motta meldinger fra gruppechatten og svare på meldinger fra andre agenter.

Dette mønsteret kan implementeres ved bruk av en sentralisert arkitektur hvor alle meldinger rutes gjennom en sentral server, eller en desentralisert arkitektur hvor meldinger utveksles direkte.

![Gruppesamtale](../../../translated_images/no/multi-agent-group-chat.ec10f4cde556babd.webp)

### Overlevering

Dette mønsteret er nyttig når du ønsker å lage en applikasjon hvor flere agenter kan overlevere oppgaver til hverandre.

Typiske bruksområder for dette mønsteret inkluderer kundestøtte, oppgavehåndtering og arbeidsflytautomatisering.

I dette mønsteret representerer hver agent en oppgave eller et steg i en arbeidsflyt, og agentene kan overlevere oppgaver til andre agenter basert på forhåndsdefinerte regler.

![Overlevering](../../../translated_images/no/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Kollaborativ filtrering

Dette mønsteret er nyttig når du ønsker å lage en applikasjon hvor flere agenter kan samarbeide om å gi anbefalinger til brukere.

Hvorfor du vil at flere agenter skal samarbeide er fordi hver agent kan ha forskjellig ekspertise og kan bidra til anbefalingsprosessen på ulike måter.

La oss ta et eksempel hvor en bruker ønsker en anbefaling på den beste aksjen å kjøpe på aksjemarkedet.

- **Bransjeekspert**:. En agent kan være ekspert på en spesifikk bransje.
- **Teknisk analyse**: En annen agent kan være ekspert på teknisk analyse.
- **Fundamental analyse**: Og en annen agent kan være ekspert på fundamental analyse. Ved å samarbeide kan disse agentene gi en mer omfattende anbefaling til brukeren.

![Anbefaling](../../../translated_images/no/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Refusjonsprosess

Vurder et scenario hvor en kunde prøver å få refusjon for et produkt; det kan være ganske mange agenter involvert i denne prosessen, men la oss dele dem opp i agenter som er spesifikke for denne prosessen og generelle agenter som kan brukes i andre prosesser.

**Agenter spesifikke for refusjonsprosessen**:

Følgende er noen agenter som kan være involvert i refusjonsprosessen:

- **Kundeagent**: Denne agenten representerer kunden og er ansvarlig for å initiere refusjonsprosessen.
- **Selgeragent**: Denne agenten representerer selgeren og er ansvarlig for å prosessere refusjonen.
- **Betalingsagent**: Denne agenten representerer betalingsprosessen og er ansvarlig for å tilbakebetale kundens betaling.
- **Løsningsagent**: Denne agenten representerer løsningsprosessen og er ansvarlig for å løse eventuelle problemer som oppstår under refusjonsprosessen.
- **Etterlevelsesagent**: Denne agenten representerer etterlevelsesprosessen og er ansvarlig for å sikre at refusjonsprosessen overholder regelverk og retningslinjer.

**Generelle agenter**:

Disse agentene kan brukes av andre deler av virksomheten din.

- **Fraktagent**: Denne agenten representerer fraktprosessen og er ansvarlig for å sende produktet tilbake til selgeren. Denne agenten kan brukes både i refusjonsprosessen og for generell frakt av et produkt ved kjøp, for eksempel.
- **Tilbakemeldingsagent**: Denne agenten representerer tilbakemeldingsprosessen og er ansvarlig for å samle inn tilbakemeldinger fra kunden. Tilbakemelding kan innhentes til enhver tid, ikke bare under refusjonsprosessen.
- **Eskalasjonsagent**: Denne agenten representerer eskaleringsprosessen og er ansvarlig for å eskalere problemer til et høyere støttenivå. Du kan bruke denne typen agent for enhver prosess der du må eskalere et problem.
- **Varslingsagent**: Denne agenten representerer varslingsprosessen og er ansvarlig for å sende varsler til kunden i ulike stadier av refusjonsprosessen.
- **Analyseagent**: Denne agenten representerer analyseprosessen og er ansvarlig for å analysere data relatert til refusjonsprosessen.
- **Revisjonsagent**: Denne agenten representerer revisjonsprosessen og er ansvarlig for å revidere refusjonsprosessen for å sikre at den blir gjennomført korrekt.
- **Rapporteringsagent**: Denne agenten representerer rapporteringsprosessen og er ansvarlig for å generere rapporter om refusjonsprosessen.
- **Kunnskapsagent**: Denne agenten representerer kunnskapsprosessen og er ansvarlig for å vedlikeholde en kunnskapsbase med informasjon relatert til refusjonsprosessen. Denne agenten kan ha kunnskap både om refusjoner og andre deler av virksomheten.
- **Sikkerhetsagent**: Denne agenten representerer sikkerhetsprosessen og er ansvarlig for å sikre sikkerheten til refusjonsprosessen.
- **Kvalitetsagent**: Denne agenten representerer kvalitetsprosessen og er ansvarlig for å sikre kvaliteten i refusjonsprosessen.

Det er ganske mange agenter listet ovenfor, både for den spesifikke refusjonsprosessen og for de generelle agentene som kan brukes i andre deler av virksomheten din. Forhåpentligvis gir dette deg en idé om hvordan du kan beslutte hvilke agenter du skal bruke i ditt multi-agent-system.

## Oppgave

Design et multi-agent-system for en kundeserviceprosess. Identifiser agentene som er involvert i prosessen, deres roller og ansvar, og hvordan de samhandler med hverandre. Vurder både agenter som er spesifikke for kundeserviceprosessen og generelle agenter som kan brukes i andre deler av virksomheten din.
> Tenk litt før du leser følgende løsning, du kan trenge flere agenter enn du tror.

> TIP: Tenk på de forskjellige fasene i kundestøtteprosessen og vurder også agenter som trengs for ethvert system.

## Løsning

[Løsning](./solution/solution.md)

## Kunnskapssjekker

Question: Når bør du vurdere å bruke flere agenter?

- [ ] A1: Når du har en liten arbeidsmengde og en enkel oppgave.
- [ ] A2: Når du har en stor arbeidsmengde
- [ ] A3: Når du har en enkel oppgave.

[Løsningsquiz](./solution/solution-quiz.md)

## Oppsummering

I denne leksjonen har vi sett på multi-agent designmønsteret, inkludert scenarier hvor flere agenter er aktuelle, fordelene ved å bruke flere agenter i stedet for en enkelt agent, byggesteinene for å implementere multi-agent designmønsteret, og hvordan få innsikt i hvordan de ulike agentene samhandler med hverandre.

### Har du flere spørsmål om multi-agent designmønsteret?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å treffe andre deltakere, delta på kontortid og få svar på spørsmål om AI-agenter.

## Tilleggsressurser

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework-dokumentasjon</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentiske designmønstre</a>


## Forrige leksjon

[Planleggingsdesign](../07-planning-design/README.md)

## Neste leksjon

[Metakognisjon i AI-agenter](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Originaldokumentet på det opprinnelige språket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->