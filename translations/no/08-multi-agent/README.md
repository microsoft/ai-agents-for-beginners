[![Multi-Agent Design](../../../translated_images/no/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikk på bildet over for å se video av denne leksjonen)_

# Multi-agent designmønstre

Så snart du begynner å jobbe med et prosjekt som involverer flere agenter, må du vurdere multi-agent designmønsteret. Det kan imidlertid ikke være umiddelbart klart når du skal gå over til flere agenter og hva fordelene er.

## Introduksjon

I denne leksjonen ønsker vi å svare på følgende spørsmål:

- Hva er scenariene der multi-agenter er anvendelige?
- Hva er fordelene ved å bruke multi-agenter fremfor bare én enkelt agent som utfører flere oppgaver?
- Hva er byggesteinene for å implementere multi-agent designmønsteret?
- Hvordan får vi innsyn i hvordan de flere agentene samhandler med hverandre?

## Læringsmål

Etter denne leksjonen skal du kunne:

- Identifisere scenarier hvor multi-agenter passer
- Gjenkjenne fordelene med å bruke multi-agenter fremfor en enkel agent.
- Forstå byggesteinene ved implementering av multi-agent designmønsteret.

Hva er det større bildet?

*Multi-agenter er et designmønster som tillater flere agenter å samarbeide for å oppnå et felles mål*.

Dette mønsteret brukes bredt innen ulike felt, inkludert robotikk, autonome systemer, og distribuert databehandling.

## Scenarier der multi-agenter er anvendelige

Så hvilke scenarier er gode bruksområder for å bruke multi-agenter? Svaret er at det finnes mange scenarier hvor bruk av flere agenter er fordelaktig, spesielt i følgende tilfeller:

- **Store arbeidsmengder**: Store arbeidsmengder kan deles opp i mindre oppgaver og tildeles ulike agenter, noe som muliggjør parallell behandling og raskere ferdigstillelse. Et eksempel på dette er ved store databehandlingsoppgaver.
- **Komplekse oppgaver**: Komplekse oppgaver, som store arbeidsmengder, kan brytes ned i mindre deloppgaver og tildeles ulike agenter, hver spesialisert på et spesifikt aspekt av oppgaven. Et godt eksempel på dette er autonome kjøretøy der ulike agenter styrer navigasjon, hinderdeteksjon, og kommunikasjon med andre kjøretøy.
- **Mangfoldig ekspertise**: Ulike agenter kan ha varierende ekspertise, noe som gjør at de kan håndtere ulike aspekter av en oppgave mer effektivt enn en enkelt agent. Et godt eksempel er innen helsevesenet hvor agenter kan håndtere diagnostikk, behandlingsplaner og pasientovervåkning.

## Fordeler ved å bruke multi-agenter fremfor en enkelt agent

Et enkelt agent-system kan fungere bra for enkle oppgaver, men for mer komplekse oppgaver kan bruk av flere agenter gi flere fordeler:

- **Spesialisering**: Hver agent kan spesialiseres for en bestemt oppgave. Manglende spesialisering i en enkelt agent betyr at du har en agent som kan gjøre alt, men som kan bli forvirret i møte med komplekse oppgaver. Den kan for eksempel ende opp med å gjøre en oppgave den ikke er best egnet for.
- **Skalerbarhet**: Det er lettere å skalere systemer ved å legge til flere agenter fremfor å overbelaste en enkelt agent.
- **Feiltoleranse**: Hvis én agent feiler kan andre fortsette å fungere, noe som sikrer systemets pålitelighet.

La oss ta et eksempel, la oss bestille en tur for en bruker. Et enkelt agent-system måtte håndtere alle aspekter av bestillingsprosessen, fra å finne flyreiser til å bestille hoteller og leiebiler. For å oppnå dette med en enkelt agent måtte agenten ha verktøy for å håndtere alle disse oppgavene. Dette kunne føre til et komplekst og monolittisk system som er vanskelig å vedlikeholde og skalere. Et multi-agent system kunne derimot hatt ulike agenter spesialisert for å finne flyreiser, bestille hoteller og leiebiler. Dette ville gjøre systemet mer modulært, lettere å vedlikeholde og skalerbart.

Sammenlign dette med et reisebyrå drevet som en enkeltbutikk versus et reisebyrå drevet som en franchise. Enkeltbutikken ville hatt en enkelt agent som håndterer alle aspekter av bestillingsprosessen, mens franchisen ville hatt ulike agenter som håndterer forskjellige deler av bestillingsprosessen.

## Byggesteiner for implementering av multi-agent designmønster

Før du kan implementere multi-agent designmønsteret, må du forstå byggesteinene som utgjør mønsteret.

La oss gjøre dette mer konkret ved å igjen se på eksempelet med å bestille en tur for en bruker. I dette tilfellet vil byggesteinene inkludere:

- **Agentkommunikasjon**: Agenter for å finne flyreiser, bestille hoteller og leiebiler må kommunisere og dele informasjon om brukerens preferanser og begrensninger. Du må bestemme hvilke protokoller og metoder som skal brukes for denne kommunikasjonen. Konkret betyr dette at agenten som finner flyreiser må kommunisere med agenten som bestiller hoteller for å sikre at hotellet bestilles for de samme datoene som flyreisen. Det innebærer at agentene må dele informasjon om brukerens reisedatoer, noe som betyr at du må bestemme *hvilke agenter som deler info og hvordan de deler info*.
- **Koordineringsmekanismer**: Agentene må koordinere sine handlinger for å sikre at brukerens preferanser og begrensninger blir møtt. En preferanse kan være at de ønsker et hotell nær flyplassen, mens en begrensning kan være at leiebiler kun er tilgjengelige på flyplassen. Dette betyr at agenten som bestiller hoteller må koordinere med agenten som bestiller leiebiler for å sikre at brukerens preferanser og begrensninger oppfylles. Dette betyr at du må bestemme *hvordan agentene koordinerer sine handlinger*.
- **Agentarkitektur**: Agentene må ha en intern struktur for å kunne ta beslutninger og lære av sine interaksjoner med brukeren. Dette betyr at agenten som finner flyreiser må ha en intern struktur for å kunne ta beslutninger om hvilke flyreiser som skal anbefales brukeren. Dette betyr at du må bestemme *hvordan agentene tar beslutninger og lærer av interaksjonene med brukeren*. Eksempler på hvordan en agent lærer og forbedres kan være at agenten som finner flyreiser kan bruke en maskinlæringsmodell for å anbefale flyreiser til brukeren basert på tidligere preferanser.
- **Innsyn i multi-agent interaksjoner**: Du må ha innsyn i hvordan de flere agentene samhandler med hverandre. Dette betyr at du trenger verktøy og teknikker for å spore agentenes aktiviteter og interaksjoner. Dette kan være i form av logg- og overvåkingsverktøy, visualiseringsverktøy og ytelsesmetrikker.
- **Multi-agent mønstre**: Det finnes ulike mønstre for implementering av multi-agent systemer, som sentraliserte, desentraliserte og hybride arkitekturer. Du må bestemme hvilket mønster som passer best for ditt brukstilfelle.
- **Mennesket i løkken**: I de fleste tilfeller vil du ha et menneske i løkken og du må instruere agentene når de skal be om menneskelig inngripen. Dette kan være i form av at en bruker ber om et spesifikt hotell eller fly som agentene ikke har anbefalt, eller ber om bekreftelse før en fly- eller hotellbestilling.

## Innsyn i multi-agent interaksjoner

Det er viktig at du har innsyn i hvordan de flere agentene samhandler med hverandre. Dette innsynet er essensielt for feilsøking, optimalisering og for å sikre den overordnede systemets effektivitet. For å oppnå dette trenger du verktøy og teknikker for å spore agentenes aktiviteter og interaksjoner. Dette kan være i form av logg- og overvåkingsverktøy, visualiseringsverktøy og ytelsesmetrikker.

For eksempel, i tilfellet med å bestille en tur for en bruker, kan du ha et dashbord som viser status for hver agent, brukerens preferanser og begrensninger, og interaksjonene mellom agentene. Dette dashbordet kan vise brukerens reisedatoer, flyene som flyagenten anbefaler, hotellene som hotellagenten anbefaler, og leiebilene som leiebilagenten anbefaler. Dette gir deg en klar oversikt over hvordan agentene samhandler og om brukerens preferanser og begrensninger blir oppfylt.

La oss se nærmere på hver av disse aspektene.

- **Logg- og overvåkingsverktøy**: Du ønsker å ha loggføring for hver handling en agent utfører. En loggoppføring kan lagre informasjon om agenten som utførte handlingen, handlingen som ble utført, tidspunktet den ble utført, og utfallet av handlingen. Denne informasjonen kan brukes til feilsøking, optimalisering og mer.

- **Visualiseringsverktøy**: Visualiseringsverktøy kan hjelpe deg å se interaksjonene mellom agentene på en mer intuitiv måte. For eksempel kan du ha en graf som viser informasjonsflyten mellom agentene. Dette kan hjelpe deg å identifisere flaskehalser, ineffektiviteter og andre problemer i systemet.

- **Ytelsesmetrikker**: Ytelsesmetrikker kan hjelpe deg med å følge systemets effektivitet. For eksempel kan du følge tiden det tar å fullføre en oppgave, antall oppgaver fullført per tidsenhet, og nøyaktigheten av anbefalingene fra agentene. Denne informasjonen kan hjelpe deg å identifisere forbedringsområder og optimalisere systemet.

## Multi-agent mønstre

La oss se på noen konkrete mønstre vi kan bruke for å lage multi-agent apper. Her er noen interessante mønstre verdt å vurdere:

### Gruppesamtale

Dette mønsteret er nyttig når du ønsker å lage en gruppechat-applikasjon hvor flere agenter kan kommunisere med hverandre. Typiske bruksområder for dette mønsteret inkluderer team-samarbeid, kundestøtte og sosiale nettverk.

I dette mønsteret representerer hver agent en bruker i gruppechatten, og meldinger sendes mellom agentene ved hjelp av en meldingsprotokoll. Agentene kan sende meldinger til gruppechatten, motta meldinger fra gruppechatten, og svare på meldinger fra andre agenter.

Dette mønsteret kan implementeres ved hjelp av en sentralisert arkitektur hvor alle meldinger går gjennom en sentral server, eller en desentralisert arkitektur hvor meldinger utveksles direkte.

![Group chat](../../../translated_images/no/multi-agent-group-chat.ec10f4cde556babd.webp)

### Overlevering

Dette mønsteret er nyttig når du ønsker å lage en applikasjon hvor flere agenter kan overlevere oppgaver til hverandre.

Typiske bruksområder for dette mønsteret inkluderer kundestøtte, oppgavehåndtering og arbeidsflytautomatisering.

I dette mønsteret representerer hver agent en oppgave eller et trinn i en arbeidsflyt, og agentene kan overlevere oppgaver til andre agenter basert på forhåndsdefinerte regler.

![Hand off](../../../translated_images/no/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Samarbeidende filtrering

Dette mønsteret er nyttig når du ønsker å lage en applikasjon hvor flere agenter kan samarbeide om å gi anbefalinger til brukere.

Grunnen til at du vil at flere agenter skal samarbeide er at hver agent kan ha ulik ekspertise og kan bidra til anbefalingsprosessen på forskjellige måter.

La oss ta et eksempel hvor en bruker ønsker en anbefaling om den beste aksjen å kjøpe på børsen.

- **Bransjeekspert**: En agent kan være ekspert på en spesifikk bransje.
- **Teknisk analyse**: En annen agent kan være ekspert på teknisk analyse.
- **Fundamental analyse**: og en annen agent kan være ekspert på fundamental analyse. Ved å samarbeide kan disse agentene gi en mer helhetlig anbefaling til brukeren.

![Recommendation](../../../translated_images/no/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Refusjonsprosess

Tenk deg et scenario hvor en kunde prøver å få refusjon for et produkt, det kan være ganske mange agenter involvert i denne prosessen men la oss dele opp mellom agenter spesifikke for denne prosessen og generelle agenter som kan brukes i andre prosesser.

**Agenter spesifikke for refusjonsprosessen**:

Følgende agenter kan være involvert i refusjonsprosessen:

- **Kunde-agent**: Denne agenten representerer kunden og er ansvarlig for å initiere refusjonsprosessen.
- **Selger-agent**: Denne agenten representerer selgeren og er ansvarlig for å behandle refusjonen.
- **Betalings-agent**: Denne agenten representerer betalingsprosessen og er ansvarlig for å refundere kundens betaling.
- **Løsnings-agent**: Denne agenten representerer løsningsprosessen og er ansvarlig for å løse eventuelle problemer som oppstår under refusjonsprosessen.
- **Regelefterlevelses-agent**: Denne agenten representerer etterlevelsesprosessen og er ansvarlig for å sikre at refusjonsprosessen følger regler og retningslinjer.

**Generelle agenter**:

Disse agentene kan brukes i andre deler av virksomheten din.

- **Frakt-agent**: Denne agenten representerer fraktprosessen og er ansvarlig for å sende produktet tilbake til selgeren. Denne agenten kan brukes både i refusjonsprosessen og for generell forsendelse av et produkt via et kjøp for eksempel.
- **Tilbakemeldings-agent**: Denne agenten representerer tilbakemeldingsprosessen og er ansvarlig for å innhente tilbakemeldinger fra kunden. Tilbakemelding kan gis når som helst, ikke bare under refusjonsprosessen.
- **Eskalerings-agent**: Denne agenten representerer eskaleringsprosessen og er ansvarlig for å eskalere problemer til et høyere supportnivå. Du kan bruke denne typen agent i enhver prosess hvor du trenger å eskalere et problem.
- **Varslings-agent**: Denne agenten representerer varslingsprosessen og er ansvarlig for å sende varsler til kunden på ulike stadier i refusjonsprosessen.
- **Analyse-agent**: Denne agenten representerer analyseprosessen og er ansvarlig for å analysere data knyttet til refusjonsprosessen.
- **Revisjons-agent**: Denne agenten representerer revisjonsprosessen og er ansvarlig for å revidere refusjonsprosessen for å sikre at den gjennomføres korrekt.
- **Rapporterings-agent**: Denne agenten representerer rapporteringsprosessen og er ansvarlig for å generere rapporter om refusjonsprosessen.
- **Kunnskaps-agent**: Denne agenten representerer kunnskapsprosessen og er ansvarlig for å vedlikeholde en kunnskapsdatabase med informasjon relatert til refusjonsprosessen. Denne agenten kan ha kunnskap både om refusjoner og andre deler av virksomheten din.
- **Sikkerhets-agent**: Denne agenten representerer sikkerhetsprosessen og er ansvarlig for å sikre sikkerheten til refusjonsprosessen.
- **Kvalitet-agent**: Denne agenten representerer kvalitetsprosessen og er ansvarlig for å sikre kvaliteten på refusjonsprosessen.

Det er ganske mange agenter listet opp tidligere både for den spesifikke refusjonsprosessen og også for de generelle agentene som kan brukes i andre deler av virksomheten din. Forhåpentligvis gir dette deg en idé om hvordan du kan avgjøre hvilke agenter du skal bruke i ditt multi-agent system.

## Oppgave

Design et multi-agent system for en kundestøtteprosess. Identifiser agentene involvert i prosessen, deres roller og ansvar, og hvordan de samhandler med hverandre. Vurder både agenter spesifikke for kundestøtteprosessen og generelle agenter som kan brukes i andre deler av virksomheten din.


> Tenk litt før du leser løsningen nedenfor, du kan trenge flere agenter enn du tror.

> TIP: Tenk på de ulike stadiene i kundestøtteprosessen og vurder også agenter som trengs for systemet.

## Løsning

[Løsning](./solution/solution.md)

## Kunnskapssjekker

### Spørsmål 1

Hvilket scenario passer best for et multi-agent system?

- [ ] A1: En støttebot svarer på vanlige spørsmål ved å bruke én kunnskapsbase og et lite sett verktøy.
- [ ] A2: En refusjonsflyt krever separate roller for svindel, betaling og samsvar, hver med sine egne verktøy, og resultatene må koordineres.
- [ ] A3: Den samme enkle klassifikasjonsforespørselen kommer tusenvis av ganger i timen.

### Spørsmål 2

Når er én enkelt agent vanligvis det beste valget?

- [ ] A1: Oppgaven kan håndteres med ett sett instruksjoner og verktøy, uten spesialistoverganger.
- [ ] A2: Agenten har tilgang til mer enn ett verktøy.
- [ ] A3: Arbeidsflyten krever separate roller med ulike tillatelser og uavhengige revisjonsspor.

[Løsning quiz](./solution/solution-quiz.md)

## Sammendrag

I denne leksjonen har vi sett på multi-agent designmønsteret, inkludert scenarier hvor multi-agenter er anvendelige, fordelene ved å bruke multi-agenter fremfor en enkelt agent, byggesteinene for å implementere multi-agent designmønsteret, og hvordan man får oversikt over hvordan de flere agentene samhandler.

### Har du flere spørsmål om Multi-Agent Design Pattern?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine spørsmål om AI-agenter.

## Ytterligere ressurser

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokumentasjon</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentiske designmønstre</a>


## Forrige leksjon

[Planleggingsdesign](../07-planning-design/README.md)

## Neste leksjon

[Metakognisjon i AI-agenter](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->