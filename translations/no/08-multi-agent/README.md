[![Multi-Agent Design](../../../translated_images/no/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikk på bildet ovenfor for å se video av denne leksen)_

# Multi-agent designmønstre

Så snart du begynner å jobbe på et prosjekt som involverer flere agenter, må du vurdere multi-agent designmønsteret. Det kan imidlertid ikke være umiddelbart klart når man skal bytte til multi-agenter og hvilke fordeler det gir.

## Introduksjon

I denne leksen ønsker vi å svare på følgende spørsmål:

- Hvilke scenarier er multi-agenter anvendelige i?
- Hva er fordelene med å bruke multi-agenter fremfor bare én enkelt agent som gjør flere oppgaver?
- Hva er byggesteinene for implementering av multi-agent designmønster?
- Hvordan får vi oversikt over hvordan de flere agentene samhandler med hverandre?

## Læringsmål

Etter denne leksen bør du kunne:

- Identifisere scenarier der multi-agenter er anvendelige
- Gjenkjenne fordelene ved å bruke multi-agenter kontra en enkelt agent.
- Forstå byggesteinene for implementering av multi-agent designmønster.

Hva er det store bildet?

*Multi-agenter er et designmønster som gjør det mulig for flere agenter å samarbeide for å oppnå et felles mål*.

Dette mønsteret brukes mye i ulike felt, inkludert robotikk, autonome systemer og distribuert databehandling.

## Scenarier hvor multi-agenter er anvendelige

Så hvilke scenarier er et godt brukstilfelle for å bruke multi-agenter? Svaret er at det finnes mange scenarier der bruk av flere agenter er fordelaktig, spesielt i følgende tilfeller:

- **Store arbeidsmengder**: Store arbeidsmengder kan deles opp i mindre oppgaver og tildeles ulike agenter, noe som muliggjør parallell behandling og raskere ferdigstillelse. Et eksempel på dette er i tilfeller med tung databehandling.
- **Komplekse oppgaver**: Komplekse oppgaver, som store arbeidsmengder, kan deles opp i mindre underoppgaver og tildeles forskjellige agenter, der hver spesialiserer seg på et bestemt aspekt av oppgaven. Et godt eksempel er for autonome kjøretøy hvor ulike agenter håndterer navigasjon, hindringsdeteksjon og kommunikasjon med andre kjøretøy.
- **Mangfoldig ekspertise**: Ulike agenter kan ha ulik ekspertise, som gjør at de kan håndtere forskjellige aspekter av en oppgave mer effektivt enn en enkelt agent. For dette tilfellet er et godt eksempel helsevesenet, der agenter kan håndtere diagnostikk, behandlingsplaner og pasientovervåkning.

## Fordeler ved bruk av multi-agenter kontra en enkelt agent

En enkelt agent kan fungere godt for enkle oppgaver, men for mer komplekse oppgaver kan bruk av flere agenter gi flere fordeler:

- **Spesialisering**: Hver agent kan være spesialisert for en bestemt oppgave. Manglende spesialisering i en enkelt agent fører til at man har en agent som kan gjøre alt, men som kan bli forvirret når den møter en kompleks oppgave. Den kan for eksempel ende opp med å utføre en oppgave den ikke er best egnet til.
- **Skalerbarhet**: Det er lettere å skalere systemer ved å legge til flere agenter enn å overbelaste en enkelt agent.
- **Feiltoleranse**: Hvis én agent feiler, kan andre fortsette å fungere, noe som sikrer systemets pålitelighet.

La oss ta et eksempel: la oss bestille en reise for en bruker. Et system med en enkelt agent måtte håndtere alle aspekter av reisebestillingsprosessen, fra å finne fly til å bestille hotell og leiebil. For å oppnå dette med en enkelt agent, måtte agenten ha verktøy for å håndtere alle disse oppgavene. Dette kunne føre til et komplekst og monolittisk system som er vanskelig å vedlikeholde og skalere. Et multi-agent-system, derimot, kunne ha ulike agenter som er spesialisert på henholdsvis flybestilling, hotellbestilling og leiebilbestilling. Dette ville gjøre systemet mer modulært, enklere å vedlikeholde og skalerbart.

Sammenlign dette med et reisebyrå drevet som en liten familiebedrift kontra et reisebyrå drevet som en franchise. Familiebedriften ville hatt en enkelt agent som håndterer alle aspekter av reisebestillingen, mens franchisen ville hatt forskjellige agenter som håndterer ulike deler av prosessen.

## Byggesteiner for implementering av multi-agent designmønster

Før du kan implementere multi-agent designmønsteret, må du forstå byggesteinene som utgjør mønsteret.

La oss konkretisere dette med igjen å se på eksemplet med å bestille en reise for en bruker. Her vil byggesteinene inkludere:

- **Agentkommunikasjon**: Agenter for å finne fly, bestille hotell og leiebil må kommunisere og dele informasjon om brukerens preferanser og begrensninger. Du må bestemme protokollene og metodene for denne kommunikasjonen. Konkrett betyr dette at agenten som finner flyvninger må kommunisere med agenten som bestiller hotell for å sikre at hotellet bestilles for de samme datoene som flyvningen. Det betyr at agentene må dele informasjon om brukerens reisedatoer, noe som krever at du bestemmer *hvilke agenter som deler info og hvordan de deler den*.
- **Koordineringsmekanismer**: Agentene må koordinere sine handlinger for å sikre at brukerens preferanser og begrensninger ivaretas. En brukerpreferanse kan være at de ønsker et hotell nær flyplassen, mens en begrensning kan være at leiebilene kun er tilgjengelige på flyplassen. Dette betyr at agenten som bestiller hotell må koordinere med agenten som bestiller leiebil for å sikre at brukerens preferanser og begrensninger oppfylles. Det betyr at du må avgjøre *hvordan agentene koordinerer sine handlinger*.
- **Agentarkitektur**: Agentene må ha en intern struktur for å kunne ta beslutninger og lære av interaksjoner med brukeren. Dette betyr at agenten som finner fly må ha intern struktur for å ta beslutninger om hvilke flyvninger som skal anbefales til brukeren. Det betyr at du må bestemme *hvordan agentene tar beslutninger og lærer av interaksjoner med brukeren*. Eksempler på hvordan en agent lærer og forbedrer seg kan være at agenten for å finne fly kan bruke en maskinlæringsmodell for å anbefale fly basert på tidligere preferanser hos brukeren.
- **Oversikt over multi-agent-interaksjoner**: Du må ha oversikt over hvordan de mange agentene samhandler med hverandre. Dette krever verktøy og teknikker for å spore agentenes aktiviteter og interaksjoner. Dette kan være i form av logg- og overvåkningsverktøy, visualiseringsverktøy og ytelsesmetrikker.
- **Multi-agent mønstre**: Det finnes ulike mønstre for implementering av multi-agent systemer, slik som sentralisert, desentralisert og hybride arkitekturer. Du må velge mønsteret som passer best til ditt brukstilfelle.
- **Mennesket i løkken**: I de fleste tilfeller vil det være et menneske involvert, og du må instruere agentene når de skal be om menneskelig inngripen. Dette kan være i form av at en bruker ber om et spesifikt hotell eller fly som agentene ikke har anbefalt eller ber om bekreftelse før fly- eller hotellbestilling.

## Oversikt over multi-agent-interaksjoner

Det er viktig at du har oversikt over hvordan de flere agentene interagerer med hverandre. Denne oversikten er nødvendig for feilsøking, optimalisering og for å sikre effektiviteten i systemet. For å oppnå dette trenger du verktøy og teknikker for å spore agentenes aktiviteter og interaksjoner. Dette kan være i form av logg- og overvåkningsverktøy, visualiseringsverktøy og ytelsesmetrikker.

For eksempel, i forbindelse med bestilling av en reise for en bruker, kan du ha et dashbord som viser status for hver agent, brukerens preferanser og begrensninger, samt interaksjonene mellom agentene. Dette dashbordet kan vise brukerens reisedatoer, flyene som er anbefalt av fly-agenten, hotellene som anbefales av hotel-agenten, og leiebilene som anbefales av leiebil-agenten. Dette gir deg en tydelig oversikt over hvordan agentene samhandler og om brukerens preferanser og begrensninger blir oppfylt.

La oss se nærmere på hver av disse aspektene.

- **Logg- og overvåkningsverktøy**: Du ønsker å logge hver handling som en agent utfører. En loggoppføring kan lagre informasjon om hvilken agent som utførte handlingen, hvilken handling som ble utført, tidspunktet for handlingen, samt utfallet av handlingen. Denne informasjonen kan brukes til feilsøking, optimalisering og mer.
- **Visualiseringsverktøy**: Visualiseringsverktøy kan hjelpe deg å se interaksjonene mellom agentene på en mer intuitiv måte. For eksempel kan du ha en graf som viser informasjonsflyten mellom agentene. Dette kan hjelpe deg å identifisere flaskehalser, ineffektivitet og andre problemer i systemet.
- **Ytelsesmetrikker**: Ytelsesmetrikker kan hjelpe deg å spore effektiviteten til multi-agent systemet. Du kan for eksempel måle tiden det tar å fullføre en oppgave, antall oppgaver fullført per tidsenhet, og nøyaktigheten av anbefalingene som gjøres av agentene. Denne informasjonen kan hjelpe deg å identifisere forbedringsområder og optimalisere systemet.

## Multi-agent mønstre

La oss gå inn på noen konkrete mønstre vi kan bruke for å lage multi-agent apper. Her er noen interessante mønstre verdt å vurdere:

### Gruppechat

Dette mønsteret er nyttig når du vil lage en gruppechatapplikasjon der flere agenter kan kommunisere med hverandre. Typiske bruksområder for dette mønsteret inkluderer teamsamarbeid, kundestøtte og sosiale nettverk.

I dette mønsteret representerer hver agent en bruker i gruppechatten, og meldinger utveksles mellom agentene ved hjelp av en meldingsprotokoll. Agentene kan sende meldinger til gruppechatten, motta meldinger fra gruppechatten og svare på meldinger fra andre agenter.

Dette mønsteret kan implementeres med en sentralisert arkitektur der alle meldinger rutes gjennom en sentral server, eller en desentralisert arkitektur der meldinger utveksles direkte.

![Group chat](../../../translated_images/no/multi-agent-group-chat.ec10f4cde556babd.webp)

### Overlevering (Hand-off)

Dette mønsteret er nyttig når du vil lage en applikasjon hvor flere agenter kan overføre oppgaver til hverandre.

Typiske bruksområder for dette inkluderer kundestøtte, oppgavehåndtering og arbeidsflytautomatikk.

I dette mønsteret representerer hver agent en oppgave eller et steg i en arbeidsflyt, og agentene kan overføre oppgaver til andre agenter basert på forhåndsdefinerte regler.

![Hand off](../../../translated_images/no/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Samarbeidende filtrering

Dette mønsteret er nyttig når du vil lage en applikasjon hvor flere agenter kan samarbeide om å gi anbefalinger til brukere.

Grunnen til at man vil at flere agenter skal samarbeide er at hver agent kan ha ulik ekspertise og kan bidra til anbefalingsprosessen på ulike måter.

La oss ta et eksempel hvor en bruker ønsker en anbefaling om den beste aksjen å kjøpe på børsen.

- **Bransjeekspert**: Én agent kan være ekspert på en spesifikk bransje.
- **Teknisk analyse**: En annen agent kan være ekspert på teknisk analyse.
- **Fundamental analyse**: En annen agent kan være ekspert på fundamental analyse. Ved å samarbeide kan disse agentene gi en mer helhetlig anbefaling til brukeren.

![Recommendation](../../../translated_images/no/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenario: Refunderingsprosess

Tenk deg et scenario hvor en kunde prøver å få refundert et produkt, det kan være flere agenter involvert i denne prosessen, men la oss dele opp mellom agenter spesifikke for denne prosessen og generelle agenter som kan brukes i andre prosesser.

**Agenter spesifikke for refunderingsprosessen**:

Følgende er noen agenter som kunne være involvert i refunderingsprosessen:

- **Kundeagent**: Denne agenten representerer kunden og er ansvarlig for å initiere refunderingsprosessen.
- **Selgeragent**: Denne agenten representerer selgeren og er ansvarlig for å behandle refusjonen.
- **Betalingsagent**: Denne agenten representerer betalingsprosessen og er ansvarlig for å refundere kundens betaling.
- **Løsningsagent**: Denne agenten representerer løsningsprosessen og er ansvarlig for å løse eventuelle problemer som oppstår under refunderingsprosessen.
- **Overholdelsesagent**: Denne agenten representerer etterlevelsesprosessen og sørger for at refunderingsprosessen følger lover og regler.

**Generelle agenter**:

Disse agentene kan brukes i andre deler av virksomheten din.

- **Shippingagent**: Denne agenten representerer fraktprosessen og er ansvarlig for å sende produktet tilbake til selgeren. Denne agenten kan brukes både for refunderingsprosessen og for generell frakt av et produkt ved for eksempel et kjøp.
- **Tilbakemeldingsagent**: Denne agenten representerer tilbakemeldingsprosessen og er ansvarlig for å samle tilbakemeldinger fra kunden. Tilbakemeldinger kan gis når som helst, ikke kun under refunderingsprosessen.
- **Eskaleringsagent**: Denne agenten representerer eskaleringsprosessen og har ansvar for å eskalere problemer til høyere supportnivå. Du kan bruke denne typen agent for enhver prosess der du må eskalere et problem.
- **Varslingsagent**: Denne agenten representerer varslingsprosessen og sørger for å sende varsler til kunden i ulike stadier av refunderingsprosessen.
- **Analyseagent**: Denne agenten representerer analyseprosessen og ansvarer for å analysere data relatert til refunderingsprosessen.
- **Revisjonsagent**: Denne agenten representerer revisjonsprosessen og sørger for at refunderingsprosessen blir gjennomført korrekt.
- **Rapporteringsagent**: Denne agenten representerer rapporteringsprosessen og genererer rapporter om refunderingsprosessen.
- **Kunnskapsagent**: Denne agenten representerer kunnskapsprosessen og vedlikeholder en kunnskapsbase med informasjon relatert til refunderingsprosessen. Denne agenten kan ha kunnskap både om refusjoner og andre deler av virksomheten.
- **Sikkerhetsagent**: Denne agenten representerer sikkerhetsprosessen og sikrer sikkerheten i refunderingsprosessen.
- **Kvalitetsagent**: Denne agenten representerer kvalitetsprosessen og sørger for kvaliteten i refunderingsprosessen.

Det er ganske mange agenter listet opp tidligere, både for den spesifikke refunderingsprosessen, men også for generelle agenter som kan brukes i andre deler av virksomheten. Forhåpentligvis gir dette deg en idé om hvordan du kan velge hvilke agenter som skal brukes i ditt multi-agent system.

## Oppgave

Design et multi-agent system for en kundestøtteprosess. Identifiser agentene som er involvert i prosessen, deres roller og ansvar, og hvordan de samhandler med hverandre. Ta i betraktning både agenter som er spesifikke for kundestøtteprosessen og generelle agenter som kan brukes i andre deler av virksomheten.
> Tenk deg godt om før du leser følgende løsning, du kan trenge flere agenter enn du tror.

> TIP: Tenk på de ulike stadiene i kundestøtteprosessen og vurder også agenter som trengs for eventuelle systemer.

## Solution

[Solution](./solution/solution.md)

## Knowledge checks

Question: When should you consider using multi-agents?

- [ ] A1: When you have a small workload and a simple task.
- [ ] A2: When you have a large workload
- [ ] A3: When you have a simple task.

[Solution quiz](./solution/solution-quiz.md)

## Summary

I denne leksjonen har vi sett på multi-agent designmønsteret, inkludert situasjoner hvor multi-agenter er aktuelle, fordelene ved å bruke multi-agenter framfor en enkelt agent, byggesteinene for implementering av multi-agent designmønsteret, og hvordan man kan få innsikt i hvordan de flere agentene samhandler med hverandre.

### Har du flere spørsmål om Multi-Agent Designmønsteret?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på spørsmål om AI-agenter.

## Additional resources

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework documentation</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentic design patterns</a>


## Previous Lesson

[Planning Design](../07-planning-design/README.md)

## Next Lesson

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->