<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T15:50:12+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "no"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.no.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikk på bildet ovenfor for å se videoen til denne leksjonen)_

# Designmønstre for multi-agent-systemer

Så snart du begynner å jobbe med et prosjekt som involverer flere agenter, må du vurdere designmønsteret for multi-agent-systemer. Det er imidlertid ikke alltid umiddelbart klart når man skal bytte til multi-agenter og hvilke fordeler det gir.

## Introduksjon

I denne leksjonen ønsker vi å svare på følgende spørsmål:

- Hvilke scenarier er multi-agenter relevante for?
- Hva er fordelene med å bruke multi-agenter i stedet for én enkelt agent som utfører flere oppgaver?
- Hva er byggesteinene for å implementere designmønsteret for multi-agent-systemer?
- Hvordan kan vi få innsikt i hvordan de ulike agentene samhandler med hverandre?

## Læringsmål

Etter denne leksjonen skal du kunne:

- Identifisere scenarier der multi-agenter er relevante.
- Gjenkjenne fordelene med å bruke multi-agenter i stedet for én enkelt agent.
- Forstå byggesteinene for å implementere designmønsteret for multi-agent-systemer.

Hva er det store bildet?

*Multi-agenter er et designmønster som lar flere agenter samarbeide for å oppnå et felles mål.*

Dette mønsteret er mye brukt i ulike felt, inkludert robotikk, autonome systemer og distribuert databehandling.

## Scenarier der multi-agenter er relevante

Så hvilke scenarier er gode eksempler på bruk av multi-agenter? Svaret er at det finnes mange situasjoner der det er fordelaktig å bruke flere agenter, spesielt i følgende tilfeller:

- **Store arbeidsmengder**: Store arbeidsmengder kan deles opp i mindre oppgaver og tildeles ulike agenter, noe som muliggjør parallell behandling og raskere fullføring. Et eksempel på dette er en stor databehandlingsoppgave.
- **Komplekse oppgaver**: Komplekse oppgaver, som store arbeidsmengder, kan brytes ned i mindre deloppgaver og tildeles ulike agenter, der hver spesialiserer seg på en spesifikk del av oppgaven. Et godt eksempel på dette er autonome kjøretøy, der ulike agenter håndterer navigasjon, hinderdeteksjon og kommunikasjon med andre kjøretøy.
- **Mangfoldig ekspertise**: Ulike agenter kan ha ulik ekspertise, noe som gjør dem i stand til å håndtere ulike aspekter av en oppgave mer effektivt enn én enkelt agent. Et godt eksempel på dette er helsevesenet, der agenter kan håndtere diagnostikk, behandlingsplaner og pasientovervåking.

## Fordeler med å bruke multi-agenter i stedet for én enkelt agent

Et system med én enkelt agent kan fungere godt for enkle oppgaver, men for mer komplekse oppgaver kan bruk av flere agenter gi flere fordeler:

- **Spesialisering**: Hver agent kan spesialiseres for en spesifikk oppgave. Mangelen på spesialisering i én enkelt agent betyr at du har en agent som kan gjøre alt, men som kan bli forvirret når den står overfor en kompleks oppgave. Den kan for eksempel ende opp med å utføre en oppgave den ikke er best egnet for.
- **Skalerbarhet**: Det er enklere å skalere systemer ved å legge til flere agenter i stedet for å overbelaste én enkelt agent.
- **Feiltoleranse**: Hvis én agent svikter, kan andre fortsette å fungere, noe som sikrer systemets pålitelighet.

La oss ta et eksempel: la oss bestille en reise for en bruker. Et system med én enkelt agent må håndtere alle aspekter av prosessen, fra å finne flyreiser til å bestille hoteller og leiebiler. For å oppnå dette med én enkelt agent, må agenten ha verktøy for å håndtere alle disse oppgavene. Dette kan føre til et komplekst og monolittisk system som er vanskelig å vedlikeholde og skalere. Et system med flere agenter, derimot, kan ha ulike agenter som er spesialiserte på å finne flyreiser, bestille hoteller og leiebiler. Dette vil gjøre systemet mer modulært, enklere å vedlikeholde og skalerbart.

Sammenlign dette med et reisebyrå drevet som en liten familiebedrift versus et reisebyrå drevet som en franchise. Familiebedriften vil ha én enkelt agent som håndterer alle aspekter av prosessen, mens franchisen vil ha ulike agenter som håndterer ulike aspekter av prosessen.

## Byggesteiner for å implementere designmønsteret for multi-agent-systemer

Før du kan implementere designmønsteret for multi-agent-systemer, må du forstå byggesteinene som utgjør mønsteret.

La oss gjøre dette mer konkret ved igjen å se på eksempelet med å bestille en reise for en bruker. I dette tilfellet vil byggesteinene inkludere:

- **Agentkommunikasjon**: Agenter for å finne flyreiser, bestille hoteller og leiebiler må kommunisere og dele informasjon om brukerens preferanser og begrensninger. Du må bestemme protokoller og metoder for denne kommunikasjonen. Dette betyr konkret at agenten for å finne flyreiser må kommunisere med agenten for å bestille hoteller for å sikre at hotellet er bestilt for de samme datoene som flyreisen. Det betyr at agentene må dele informasjon om brukerens reisedatoer, noe som betyr at du må bestemme *hvilke agenter som deler informasjon og hvordan de deler informasjon*.
- **Koordineringsmekanismer**: Agenter må koordinere sine handlinger for å sikre at brukerens preferanser og begrensninger blir oppfylt. En brukerpreferanse kan være at de ønsker et hotell nær flyplassen, mens en begrensning kan være at leiebiler kun er tilgjengelige på flyplassen. Dette betyr at agenten for å bestille hoteller må koordinere med agenten for å bestille leiebiler for å sikre at brukerens preferanser og begrensninger blir oppfylt. Dette betyr at du må bestemme *hvordan agentene koordinerer sine handlinger*.
- **Agentarkitektur**: Agenter må ha en intern struktur for å ta beslutninger og lære av sine interaksjoner med brukeren. Dette betyr at agenten for å finne flyreiser må ha en intern struktur for å ta beslutninger om hvilke flyreiser som skal anbefales til brukeren. Dette betyr at du må bestemme *hvordan agentene tar beslutninger og lærer av sine interaksjoner med brukeren*. Eksempler på hvordan en agent lærer og forbedrer seg kan være at agenten for å finne flyreiser bruker en maskinlæringsmodell for å anbefale flyreiser til brukeren basert på deres tidligere preferanser.
- **Innsikt i multi-agent-interaksjoner**: Du må ha innsikt i hvordan de ulike agentene samhandler med hverandre. Dette betyr at du må ha verktøy og teknikker for å spore agentaktiviteter og interaksjoner. Dette kan være i form av loggings- og overvåkingsverktøy, visualiseringsverktøy og ytelsesmålinger.
- **Multi-agent-mønstre**: Det finnes ulike mønstre for å implementere multi-agent-systemer, som sentraliserte, desentraliserte og hybride arkitekturer. Du må bestemme mønsteret som passer best til ditt brukstilfelle.
- **Menneske i loopen**: I de fleste tilfeller vil du ha et menneske i loopen, og du må instruere agentene om når de skal be om menneskelig intervensjon. Dette kan være i form av en bruker som ber om et spesifikt hotell eller flyreise som agentene ikke har anbefalt, eller som ber om bekreftelse før de bestiller en flyreise eller et hotell.

## Innsikt i multi-agent-interaksjoner

Det er viktig at du har innsikt i hvordan de ulike agentene samhandler med hverandre. Denne innsikten er avgjørende for feilsøking, optimalisering og for å sikre systemets samlede effektivitet. For å oppnå dette må du ha verktøy og teknikker for å spore agentaktiviteter og interaksjoner. Dette kan være i form av loggings- og overvåkingsverktøy, visualiseringsverktøy og ytelsesmålinger.

For eksempel, i tilfelle av å bestille en reise for en bruker, kan du ha et dashbord som viser statusen til hver agent, brukerens preferanser og begrensninger, og interaksjonene mellom agentene. Dette dashbordet kan vise brukerens reisedatoer, flyreisene anbefalt av flyagenten, hotellene anbefalt av hotellagenten, og leiebilene anbefalt av leiebilagenten. Dette vil gi deg en klar oversikt over hvordan agentene samhandler med hverandre og om brukerens preferanser og begrensninger blir oppfylt.

La oss se nærmere på hver av disse aspektene.

- **Loggings- og overvåkingsverktøy**: Du vil ha logging for hver handling utført av en agent. En loggoppføring kan lagre informasjon om agenten som utførte handlingen, handlingen som ble utført, tidspunktet handlingen ble utført, og resultatet av handlingen. Denne informasjonen kan deretter brukes til feilsøking, optimalisering og mer.

- **Visualiseringsverktøy**: Visualiseringsverktøy kan hjelpe deg med å se interaksjonene mellom agenter på en mer intuitiv måte. For eksempel kan du ha en graf som viser informasjonsflyten mellom agenter. Dette kan hjelpe deg med å identifisere flaskehalser, ineffektivitet og andre problemer i systemet.

- **Ytelsesmålinger**: Ytelsesmålinger kan hjelpe deg med å spore effektiviteten til multi-agent-systemet. For eksempel kan du spore tiden det tar å fullføre en oppgave, antall oppgaver fullført per tidsenhet, og nøyaktigheten til anbefalingene gitt av agentene. Denne informasjonen kan hjelpe deg med å identifisere forbedringsområder og optimalisere systemet.

## Multi-agent-mønstre

La oss dykke ned i noen konkrete mønstre vi kan bruke for å lage multi-agent-applikasjoner. Her er noen interessante mønstre verdt å vurdere:

### Gruppechat

Dette mønsteret er nyttig når du vil lage en gruppechat-applikasjon der flere agenter kan kommunisere med hverandre. Typiske brukstilfeller for dette mønsteret inkluderer teamarbeid, kundestøtte og sosiale nettverk.

I dette mønsteret representerer hver agent en bruker i gruppechatten, og meldinger utveksles mellom agenter ved hjelp av en meldingsprotokoll. Agentene kan sende meldinger til gruppechatten, motta meldinger fra gruppechatten og svare på meldinger fra andre agenter.

Dette mønsteret kan implementeres ved hjelp av en sentralisert arkitektur der alle meldinger rutes gjennom en sentral server, eller en desentralisert arkitektur der meldinger utveksles direkte.

![Gruppechat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.no.png)

### Overlevering

Dette mønsteret er nyttig når du vil lage en applikasjon der flere agenter kan overlevere oppgaver til hverandre.

Typiske brukstilfeller for dette mønsteret inkluderer kundestøtte, oppgavestyring og arbeidsflytautomatisering.

I dette mønsteret representerer hver agent en oppgave eller et steg i en arbeidsflyt, og agenter kan overlevere oppgaver til andre agenter basert på forhåndsdefinerte regler.

![Overlevering](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.no.png)

### Samarbeidsfiltrering

Dette mønsteret er nyttig når du vil lage en applikasjon der flere agenter kan samarbeide for å gi anbefalinger til brukere.

Hvorfor du vil ha flere agenter til å samarbeide, er fordi hver agent kan ha ulik ekspertise og kan bidra til anbefalingsprosessen på ulike måter.

La oss ta et eksempel der en bruker ønsker en anbefaling om den beste aksjen å kjøpe på aksjemarkedet.

- **Bransjeekspert**: Én agent kan være ekspert på en spesifikk bransje.
- **Teknisk analyse**: En annen agent kan være ekspert på teknisk analyse.
- **Fundamental analyse**: Og en annen agent kan være ekspert på fundamental analyse. Ved å samarbeide kan disse agentene gi en mer omfattende anbefaling til brukeren.

![Anbefaling](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.no.png)

## Scenario: Refusjonsprosess

Tenk deg et scenario der en kunde prøver å få refusjon for et produkt. Det kan være ganske mange agenter involvert i denne prosessen, men la oss dele det opp mellom agenter som er spesifikke for denne prosessen og generelle agenter som kan brukes i andre prosesser.

**Agenter spesifikke for refusjonsprosessen**:

Følgende er noen agenter som kan være involvert i refusjonsprosessen:

- **Kundeagent**: Denne agenten representerer kunden og er ansvarlig for å starte refusjonsprosessen.
- **Selgeragent**: Denne agenten representerer selgeren og er ansvarlig for å behandle refusjonen.
- **Betalingsagent**: Denne agenten representerer betalingsprosessen og er ansvarlig for å refundere kundens betaling.
- **Løsningsagent**: Denne agenten representerer løsningsprosessen og er ansvarlig for å løse eventuelle problemer som oppstår under refusjonsprosessen.
- **Compliance-agent**: Denne agenten representerer compliance-prosessen og er ansvarlig for å sikre at refusjonsprosessen overholder regler og retningslinjer.

**Generelle agenter**:

Disse agentene kan brukes av andre deler av virksomheten din.

- **Fraktagent**: Denne agenten representerer fraktprosessen og er ansvarlig for å sende produktet tilbake til selgeren. Denne agenten kan brukes både for refusjonsprosessen og for generell frakt av et produkt, for eksempel ved kjøp.
- **Tilbakemeldingsagent**: Denne agenten representerer tilbakemeldingsprosessen og er ansvarlig for å samle tilbakemeldinger fra kunden. Tilbakemeldinger kan samles inn når som helst, ikke bare under refusjonsprosessen.
- **Eskaleringsagent**: Denne agenten representerer eskaleringsprosessen og er ansvarlig for å eskalere problemer til et høyere nivå av støtte. Du kan bruke denne typen agent i enhver prosess der du trenger å eskalere et problem.
- **Varslingsagent**: Denne agenten representerer varslingsprosessen og er ansvarlig for å sende varsler til kunden på ulike stadier av refusjonsprosessen.
- **Analyseagent**: Denne agenten representerer analyseprosessen og er ansvarlig for å analysere data relatert til refusjonsprosessen.
- **Revisjonsagent**: Denne agenten representerer revisjonsprosessen og er ansvarlig for å revidere refusjonsprosessen for å sikre at den utføres korrekt.
- **Rapporteringsagent**: Denne agenten representerer rapporteringsprosessen og er ansvarlig for å generere rapporter om refusjonsprosessen.
- **Kunnskapsagent**: Denne agenten representerer kunnskapsprosessen og er ansvarlig for å opprettholde en kunnskapsbase med informasjon relatert til refusjonsprosessen. Denne agenten kan være kunnskapsrik både om refusjoner og andre deler av virksomheten din.
- **Sikkerhetsagent**: Denne agenten representerer sikkerhetsprosessen og er ansvarlig for å sikre sikkerheten til refusjonsprosessen.
- **Kvalitetsagent**: Denne agenten representerer kvalitetsprosessen og er ansvarlig for å sikre kvaliteten på refusjonsprosessen.

Det er ganske mange agenter listet opp tidligere, både for den spesifikke refusjonsprosessen og for de generelle agentene som kan brukes i andre deler av virksomheten din. Forhåpentligvis gir dette deg en idé om hvordan du kan bestemme hvilke agenter du skal bruke i ditt multi-agent-system.

## Oppgave
## Design et multi-agent system for en kundestøtteprosess. Identifiser agentene som er involvert i prosessen, deres roller og ansvar, og hvordan de samhandler med hverandre. Tenk på både agenter som er spesifikke for kundestøtteprosessen og generelle agenter som kan brukes i andre deler av virksomheten.

> Tenk litt før du leser den følgende løsningen, du kan trenge flere agenter enn du tror.

> TIP: Tenk på de forskjellige stadiene i kundestøtteprosessen og vurder også agenter som trengs for ethvert system.

## Løsning

[Løsning](./solution/solution.md)

## Kunnskapssjekk

Spørsmål: Når bør du vurdere å bruke multi-agenter?

- [ ] A1: Når du har en liten arbeidsmengde og en enkel oppgave.
- [ ] A2: Når du har en stor arbeidsmengde.
- [ ] A3: Når du har en enkel oppgave.

[Løsningsquiz](./solution/solution-quiz.md)

## Sammendrag

I denne leksjonen har vi sett på multi-agent designmønsteret, inkludert scenarier der multi-agenter er anvendelige, fordelene ved å bruke multi-agenter fremfor en enkelt agent, byggesteinene for å implementere multi-agent designmønsteret, og hvordan man kan få innsikt i hvordan de ulike agentene samhandler med hverandre.

### Har du flere spørsmål om Multi-Agent Designmønsteret?

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre elever, delta på kontortid og få svar på dine spørsmål om AI-agenter.

## Tilleggsressurser

- 

## Forrige leksjon

[Planleggingsdesign](../07-planning-design/README.md)

## Neste leksjon

[Metakognisjon i AI-agenter](../09-metacognition/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.