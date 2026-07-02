[![Agentic RAG](../../../translated_images/no/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klikk på bildet over for å se video av denne leksjonen)_

# Agentic RAG

Denne leksjonen gir en omfattende oversikt over Agentic Retrieval-Augmented Generation (Agentic RAG), et nytt AI-paradigme hvor store språkmodeller (LLM-er) autonomt planlegger sine neste steg mens de henter informasjon fra eksterne kilder. I motsetning til statiske hent-og-les-mønstre, involverer Agentic RAG iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata. Systemet evaluerer resultater, forbedrer spørringer, kaller inn flere verktøy ved behov, og fortsetter denne syklusen til en tilfredsstillende løsning oppnås.

## Introduksjon

Denne leksjonen vil dekke

- **Forstå Agentic RAG:**  Lær om det nye paradigmet i AI hvor store språkmodeller (LLM-er) autonomt planlegger sine neste steg mens de henter informasjon fra eksterne datakilder.
- **Forstå Iterativ Maker-Checker Stil:** Forstå løkken med iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata, designet for å forbedre nøyaktighet og håndtere feilaktige spørringer.
- **Utforske Praktiske Bruksområder:** Identifisere scenarier hvor Agentic RAG utmerker seg, som i miljøer med krav til korrekthet, komplekse databaseinteraksjoner, og utvidede arbeidsflyter.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du kan/forstå:

- **Forstå Agentic RAG:** Lær om det nye paradigmet i AI hvor store språkmodeller (LLM-er) autonomt planlegger sine neste steg mens de henter informasjon fra eksterne datakilder.
- **Iterativ Maker-Checker Stil:** Forstå konseptet med en løkke av iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata, designet for å forbedre nøyaktighet og håndtere feilaktige spørringer.
- **Eierskap til Resonneringsprosessen:** Forstå systemets evne til å eie sin egen resonnementprosess, ta beslutninger om hvordan det skal nærme seg problemer uten å stole på forhåndsdefinerte veier.
- **Arbeidsflyt:** Forstå hvordan en agentisk modell uavhengig bestemmer seg for å hente markedstrendrapporter, identifisere konkurrentdata, korrelere interne salgsdata, syntetisere funn og evaluere strategien.
- **Iterative Løkker, Verktøyintegrasjon og Minne:** Lær om systemets avhengighet av en løkkeinteraksjonsmodell, som opprettholder tilstand og minne gjennom trinnene for å unngå repeterende løkker og ta informerte beslutninger.
- **Håndtering av Feilmåter og Selvkorrigering:** Utforsk systemets robuste selvkorrigeringsmekanismer, inkludert iterasjon og ny forespørsel, bruk av diagnostiske verktøy, og fallback til menneskelig overvåkning.
- **Grenser for Agency:** Forstå begrensningene til Agentic RAG, med fokus på domene-spesifikk autonomi, avhengighet av infrastruktur, og respekt for retningslinjer.
- **Praktiske Bruksområder og Verdi:** Identifiser scenarier hvor Agentic RAG utmerker seg, som i miljøer med krav til korrekthet, komplekse databaseinteraksjoner og utvidede arbeidsflyter.
- **Styring, Transparens og Tillit:** Lær om viktigheten av styring og transparens, inkludert forklarlig resonnering, bias-kontroll og menneskelig tilsyn.

## Hva er Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) er et nytt AI-paradigme hvor store språkmodeller (LLM-er) autonomt planlegger sine neste steg mens de henter informasjon fra eksterne kilder. I motsetning til statiske hent-og-les-mønstre, involverer Agentic RAG iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata. Systemet evaluerer resultater, forbedrer spørringer, kaller inn flere verktøy ved behov, og fortsetter denne syklusen til en tilfredsstillende løsning oppnås. Denne iterative “maker-checker” stilen forbedrer nøyaktighet, håndterer feilaktige spørringer, og sikrer høy kvalitet på resultatene.

Systemet eier aktivt sin resonnementprosess, omskriver mislykkede spørringer, velger ulike hentemetoder, og integrerer flere verktøy — slik som vektorsøk i Azure AI Search, SQL-databaser eller tilpassede API-er — før det fullfører sitt svar. Den kjennetegnende kvaliteten ved et agentisk system er evnen til å eie sin egen resonnementprosess. Tradisjonelle RAG-implementeringer er avhengige av forhåndsdefinerte veier, men et agentisk system avgjør autonomt rekkefølgen av trinn basert på kvaliteten på informasjonen det finner.

## Definisjon av Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) er et nytt paradigme innen AI-utvikling hvor LLM-er ikke bare henter informasjon fra eksterne datakilder, men også autonomt planlegger sine neste steg. I motsetning til statiske hent-og-les-mønstre eller nøye scriptede promptsekvenser, involverer Agentic RAG en løkke med iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata. Ved hvert trinn vurderer systemet resultatene det har fått, avgjør om det skal forbedre spørringene, kaller opp flere verktøy ved behov, og fortsetter denne syklusen til en tilfredsstillende løsning oppnås.

Denne iterative “maker-checker” operasjonsstilen er designet for å forbedre nøyaktighet, håndtere feilaktige spørringer til strukturerte databaser (f.eks. NL2SQL), og sikre balanserte, høykvalitetsresultater. I stedet for å stole utelukkende på nøye utformede promptkjeder, eier systemet aktivt sin egen resonnementprosess. Det kan omskrive spørringer som feiler, velge ulike hentemetoder, og integrere flere verktøy — slik som vektorsøk i Azure AI Search, SQL-databaser eller tilpassede API-er — før det fullfører sitt svar. Dette fjerner behovet for altfor komplekse orkestreringsrammeverk. I stedet kan en relativt enkel løkke av “LLM-kall → verktøybruk → LLM-kall → …” gi sofistikerte og veldokumenterte utdata.

![Agentic RAG Core Loop](../../../translated_images/no/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Eierskap til Resonneringsprosessen

Den utpregede kvaliteten som gjør et system “agentisk” er dets evne til å eie sin resonnementprosess. Tradisjonelle RAG-implementeringer er ofte avhengige av at mennesker forhåndsdefinerer en sti for modellen: en tankerekke som beskriver hva som skal hentes og når.
Men når et system er virkelig agentisk, bestemmer det internt hvordan det nærmer seg problemet. Det utfører ikke bare et skript; det avgjør autonomt rekkefølgen av trinn basert på kvaliteten på informasjonen det finner.
For eksempel, hvis det blir bedt om å lage en produktlanseringsstrategi, stoler det ikke bare på et prompt som beskriver hele forsknings- og beslutningsarbeidsflyten. Isteden bestemmer den agentiske modellen uavhengig å:

1. Hente oppdaterte markedstrendrapporter ved hjelp av Bing Web Grounding
2. Identifisere relevant konkurrentdata med Azure AI Search.
3.	Korrelere historiske interne salgsdata med Azure SQL Database.
4. Syntetisere funnene til en sammenhengende strategi orkestrert via Azure OpenAI Service.
5.	Evaluere strategien for hull eller inkonsistenser, og be om en ny runde henting om nødvendig.
Alle disse trinnene — forbedre spørringer, velge kilder, iterere til de er “fornøyd” med svaret — besluttes av modellen, ikke forhåndsprogrammert av et menneske.

## Iterative Løkker, Verktøyintegrasjon og Minne

![Tool Integration Architecture](../../../translated_images/no/tool-integration.0f569710b5c17c10.webp)

Et agentisk system baserer seg på en løkkeinteraksjonsmodell:

- **Første kall:** Brukerens mål (altså brukerprompt) presenteres for LLM.
- **Verktøyinnkalling:** Hvis modellen identifiserer manglende informasjon eller tvetydige instruksjoner, velger den et verktøy eller en hentemetode — som et vektorbasert databasesspørsmål (f.eks. Azure AI Search Hybrid søk over private data) eller et strukturert SQL-kall — for å samle mer kontekst.
- **Vurdering & Forbedring:** Etter å ha gjennomgått de returnerte dataene, avgjør modellen om informasjonen er tilstrekkelig. Hvis ikke, forbedrer den spørringen, prøver et annet verktøy, eller justerer tilnærmingen.
- **Gjenta til tilfreds:** Denne syklusen fortsetter til modellen avgjør at den har nok klarhet og bevis for å gi et endelig, velbegrunnet svar.
- **Minne & Tilstand:** Fordi systemet opprettholder tilstand og minne gjennom trinnene, kan det huske tidligere forsøk og resultater, unngå repeterende løkker, og ta mer informerte beslutninger underveis.

Over tid skapes en følelse av utviklende forståelse, noe som gjør det mulig for modellen å navigere komplekse, flertrinnsoppgaver uten at et menneske må intervenere kontinuerlig eller omforme prompten.

## Håndtering av Feilmåter og Selvkorrigering

Agentic RAGs autonomi involverer også robuste selvkorrigeringsmekanismer. Når systemet støter på blindveier — slik som å hente irrelevante dokumenter eller møte feilaktige spørringer — kan det:

- **Iterere og Gjenta Spørring:** I stedet for å returnere lavverdige svar, prøver modellen nye søkestrategier, omskriver databasespørringer, eller ser på alternative datasett.
- **Bruke Diagnostiske Verktøy:** Systemet kan kalle inn ekstra funksjoner designet for å hjelpe det med å feilsøke sine resonnementstrinn eller bekrefte korrektheten av hentede data. Verktøy som Azure AI Tracing vil være viktige for å muliggjøre robust observasjon og overvåkning.
- **Fallback til Menneskelig Overvåkning:** For oppgaver med høye konsekvenser eller gjentatte feil kan modellen flagge usikkerhet og be om menneskelig veiledning. Når mennesket gir korrigerende tilbakemelding, kan modellen inkorporere denne lærdommen fremover.

Denne iterative og dynamiske tilnærmingen gjør at modellen kan forbedre seg kontinuerlig, og sikrer at det ikke bare er et engangssystem, men at det lærer av feil under en gitt økt.

![Self Correction Mechanism](../../../translated_images/no/self-correction.da87f3783b7f174b.webp)

## Grenser for Agency

Til tross for sin autonomi innen en oppgave, er Agentic RAG ikke analogt med kunstig generell intelligens. Dets “agentiske” evner er begrenset til verktøyene, datakildene, og retningslinjene som er gitt av menneskelige utviklere. Det kan ikke finne opp egne verktøy eller trå utenfor de domeneavgrensningene som er satt. Snarere utmerker det seg i dynamisk orkestrering av ressursene som er tilgjengelige.
Viktige forskjeller fra mer avanserte AI-former inkluderer:

1. **Domene-Spesifikk Autonomi:** Agentic RAG-systemer fokuserer på å oppnå brukerspesifiserte mål innen et kjent domene, og bruker strategier som omskriving av spørringer eller valg av verktøy for å forbedre resultater.
2. **Infrastrukturavhengig:** Systemets evner avhenger av verktøyene og dataene som utviklere har integrert. Det kan ikke overstige disse grensene uten menneskelig inngripen.
3. **Respekt for Retningslinjer:** Etiske retningslinjer, samsvarsregler, og forretningspolicyer er svært viktige. Agentens frihet er alltid begrenset av sikkerhetstiltak og tilsynsmekanismer (forhåpentligvis?)

## Praktiske Bruksområder og Verdi

Agentic RAG utmerker seg i scenarier som krever iterativ forbedring og presisjon:

1. **Riktighetsfokuserte Miljøer:** I samsvarssjekker, regulatoriske analyser eller juridisk forskning kan den agentiske modellen gjentatte ganger verifisere fakta, konsultere flere kilder, og omskrive spørringer til den har produsert et grundig vurdert svar.
2. **Komplekse Databaseinteraksjoner:** Når man jobber med strukturerte data hvor spørringer ofte kan feile eller trenge justering, kan systemet autonomt forbedre spørringene med Azure SQL eller Microsoft Fabric OneLake, og sikre at den endelige hentingen stemmer med brukerens intensjon.
3. **Utvidede Arbeidsflyter:** Lengre økter kan utvikle seg ettersom ny informasjon kommer frem. Agentic RAG kan kontinuerlig inkorporere ny data, og skifte strategier etter hvert som det lærer mer om problemområdet.

## Styring, Transparens og Tillit

Etter hvert som disse systemene blir mer autonome i sin resonnement, er styring og transparens avgjørende:

- **Forklarlig Resonnering:** Modellen kan gi et revisjonsspor over hvilke spørringer den gjorde, hvilke kilder den brukte, og hvilke resonnementstrinn den tok for å nå konklusjonen sin. Verktøy som Azure AI Content Safety og Azure AI Tracing / GenAIOps kan bidra til å opprettholde transparens og redusere risiko.
- **Bias-Kontroll og Balansert Henting:** Utviklere kan justere hentestrategier for å sikre at balanserte, representerende datakilder vurderes, og regelmessig revidere utdata for å oppdage bias eller skjevheter ved bruk av tilpassede modeller for avanserte dataorganisasjoner med Azure Machine Learning.
- **Menneskelig Tilsyn og Samsvar:** For sensitive oppgaver er menneskelig gjennomgang essensiell. Agentic RAG erstatter ikke menneskelig dømmekraft i avgjørelser med høye konsekvenser — det forsterker den ved å levere grundigere vurderte alternativer.

Det er viktig å ha verktøy som gir en klar oversikt over handlingene. Uten slike kan feilsøking av en flertrinnsprosess være svært vanskelig. Se følgende eksempel fra Literal AI (selskapet bak Chainlit) for et Agent-kjør:

![AgentRunExample](../../../translated_images/no/AgentRunExample.471a94bc40cbdc0c.webp)

## Konklusjon

Agentic RAG representerer en naturlig utvikling i hvordan AI-systemer håndterer komplekse, dataintensive oppgaver. Ved å adoptere en løkkeinteraksjonsmodell, autonomt velge verktøy, og forbedre spørringer til høy kvalitet er oppnådd, beveger systemet seg bort fra statisk promptfølgning til en mer adaptiv, kontekstsensitiv beslutningstaker. Selv med begrensninger satt av menneskedefinert infrastruktur og etiske retningslinjer, muliggjør disse agentiske egenskapene rikere, mer dynamiske, og til syvende og sist mer nyttige AI-interaksjoner for både bedrifter og sluttbrukere.

### Har du flere spørsmål om Agentic RAG?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortimer og få svar på dine AI Agents-spørsmål.

## Ekstra ressurser

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementer Retrieval Augmented Generation (RAG) med Azure OpenAI Service: Lær hvordan du bruker egne data med Azure OpenAI Service. Denne Microsoft Learn-modulen gir en omfattende guide for å implementere RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering av generative AI-applikasjoner med Microsoft Foundry: Denne artikkelen dekker evaluering og sammenligning av modeller på offentlig tilgjengelige datasett, inkludert agentiske AI-applikasjoner og RAG-arkitekturer</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Hva er Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: En komplett guide til agentbasert Retrieval Augmented Generation – Nyheter fra generasjon RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: gi kraft til RAG-en din med spørringsomformulering og selvspørring! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Legge til agentiske lag i RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Fremtiden for kunnskapsassistenter: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Hvordan bygge agentiske RAG-systemer</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Bruke Microsoft Foundry Agent Service for å skalere dine AI-agenter</a>

### Akademiske artikler

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativ forbedring med selvtilbakemelding</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Språklige agenter med verbal forsterkende læring</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Store språkmodeller kan rette seg selv med verktøy-interaktiv kritikk</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: En undersøkelse av agentisk RAG</a>

## Forrige leksjon

[Tool Use Design Pattern](../04-tool-use/README.md)

## Neste leksjon

[Bygge pålitelige AI-agenter](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->