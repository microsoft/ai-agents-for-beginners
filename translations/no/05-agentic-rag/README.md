[![Agentic RAG](../../../translated_images/no/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klikk på bildet ovenfor for å se video av denne leksjonen)_

# Agentic RAG

Denne leksjonen gir en omfattende oversikt over Agentic Retrieval-Augmented Generation (Agentic RAG), et nytt AI-paradigme der store språkmodeller (LLMs) selvstendig planlegger sine neste steg mens de henter informasjon fra eksterne kilder. I motsetning til statiske hent-og-les-mønstre involverer Agentic RAG iterative kall til LLM, blandet med verktøy- eller funksjonskall og strukturerte utdata. Systemet evaluerer resultater, forbedrer spørsmål, kaller opp flere verktøy ved behov og fortsetter denne syklusen til en tilfredsstillende løsning er oppnådd.

## Introduksjon

Denne leksjonen vil dekke

- **Forstå Agentic RAG:** Lær om det nye paradigmet i AI der store språkmodeller (LLMs) selvstendig planlegger sine neste steg mens de henter informasjon fra eksterne datakilder.
- **Forstå Iterativ Maker-Checker Stil:** Forstå løkken av iterative kall til LLM, blandet med verktøy- eller funksjonskall og strukturerte utdata, designet for å forbedre korrektheten og håndtere feilformulerte spørsmål.
- **Utforsk Praktiske Bruksområder:** Identifiser situasjoner der Agentic RAG skinner, som i miljøer med fokus på korrekthet, komplekse databaseinteraksjoner og utvidede arbeidsflyter.

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne/forstå:

- **Forstå Agentic RAG:** Lær om det nye paradigmet i AI der store språkmodeller (LLMs) selvstendig planlegger sine neste steg mens de henter informasjon fra eksterne datakilder.
- **Iterativ Maker-Checker Stil:** Forstå konseptet med en løkke av iterative kall til LLM, blandet med verktøy- eller funksjonskall og strukturerte utdata, designet for å forbedre korrektheten og håndtere feilformulerte spørsmål.
- **Eie Resonneringsprosessen:** Forstå systemets evne til å eie sin resonnementprosess og ta beslutninger om hvordan det skal nærme seg problemer uten å stole på forhåndsdefinerte veier.
- **Arbeidsflyt:** Forstå hvordan en agentisk modell selvstendig bestemmer seg for å hente markedsrapportene, identifisere konkurrentdata, korrelere interne salgsmetrikker, syntetisere funnene og evaluere strategien.
- **Iterative Løkker, Verktøyintegrasjon og Minne:** Lær om systemets avhengighet av et løkkebasert interaksjonsmønster, opprettholde tilstand og minne over trinn for å unngå repetitive løkker og ta informerte beslutninger.
- **Håndtering av Feilmodus og Selvkorrigering:** Utforsk systemets robuste selvkorrigeringsmekanismer, inkludert iterering og nyforespørsler, bruk av diagnostiske verktøy og tilbakefall til menneskelig overvåking.
- **Agentgrensesnitt:** Forstå begrensningene til Agentic RAG, med fokus på domene-spesifikk autonomi, avhengighet av infrastruktur og respekt for sikkerhetsrammer.
- **Praktiske Brukstilfeller og Verdi:** Identifiser situasjoner der Agentic RAG skinner, som i miljøer med fokus på korrekthet, komplekse databaseinteraksjoner og utvidede arbeidsflyter.
- **Styring, Transparens og Tillit:** Lær om viktigheten av styring og transparens, inkludert forklarbar resonnement, bias-kontroll og menneskelig tilsyn.

## Hva er Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) er et nytt AI-paradigme der store språkmodeller (LLMs) selvstendig planlegger sine neste steg mens de henter informasjon fra eksterne kilder. I motsetning til statiske hent-og-les-mønstre involverer Agentic RAG iterative kall til LLM, blandet med verktøy- eller funksjonskall og strukturerte utdata. Systemet evaluerer resultater, forbedrer spørsmål, kaller opp flere verktøy ved behov og fortsetter denne syklusen til en tilfredsstillende løsning er oppnådd. Denne iterative "maker-checker"-stilen forbedrer korrekthet, håndterer feilformulerte spørsmål og sikrer høy kvalitet på resultatene.

Systemet eier aktivt sin resonneringsprosess, omskriver mislykkede spørsmål, velger andre hente-metoder og integrerer flere verktøy—slik som vektorsøk i Azure AI Search, SQL-databaser eller tilpassede API-er—før det avslutter svaret. Den avgjørende kvaliteten til et agentisk system er dets evne til å eie sin resonneringsprosess. Tradisjonelle RAG-implementasjoner er avhengige av forhåndsdefinerte veier, men et agentisk system bestemmer sekvensen av steg autonomt basert på kvaliteten av informasjonen det finner.

## Definere Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) er et nytt paradigme innen AI-utvikling hvor LLM-er ikke bare henter informasjon fra eksterne datakilder, men også autonomt planlegger sine neste steg. I motsetning til statiske hent-og-les-mønstre eller nøye skriptede promptsekvenser involverer Agentic RAG en løkke av iterative kall til LLM, blandet med verktøy- eller funksjonskall og strukturerte utdata. Ved hvert steg evaluerer systemet resultatene det har fått, bestemmer om det skal forbedre spørsmålene, kaller opp flere verktøy ved behov og fortsetter denne syklusen til en tilfredsstillende løsning er oppnådd.

Denne iterative "maker-checker"-operasjonen er designet for å forbedre korrekthet, håndtere feilformulerte spørsmål mot strukturerte databaser (f.eks. NL2SQL), og sikre balanserte, høykvalitetsresultater. Istedenfor å bare stole på nøye konstruerte promptkjeder eier systemet aktivt sin resonneringsprosess. Det kan omskrive spørsmål som mislykkes, velge ulike hente-metoder og integrere flere verktøy—som vektorsøk i Azure AI Search, SQL-databaser eller tilpassede API-er—før det avslutter svaret. Dette fjerner behovet for overkompliserte orkestreringsrammeverk. Isteden kan en relativt enkel løkke av "LLM-kall → verktøybruk → LLM-kall → …" gi sofistikerte og godt funderte utdata.

![Agentic RAG Core Loop](../../../translated_images/no/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Eie resonnementprosessen

Den avgjørende kvaliteten som gjør et system "agentisk" er dets evne til å eie sin resonneringsprosess. Tradisjonelle RAG-implementasjoner er ofte avhengige av at mennesker forhåndsdefinerer en sti for modellen: en kjede av tanker som beskriver hva som skal hentes og når.
Men når et system er virkelig agentisk, bestemmer det internt hvordan det skal nærme seg problemet. Det utfører ikke bare et skript; det bestemmer autonomt sekvensen av steg basert på kvaliteten av informasjonen det finner.
For eksempel, hvis det blir bedt om å lage en produktlanseringsstrategi, stoler det ikke bare på en prompt som forklarer hele forsknings- og beslutningsprosessen. Isteden bestemmer den agentiske modellen selvstendig å:

1. Hente oppdaterte markedsrapportrapporter ved bruk av Bing Web Grounding
2. Identifisere relevant konkurrentdata ved bruk av Azure AI Search.
3.	Korrelere historiske interne salgsmetrikker ved bruk av Azure SQL Database.
4. Syntetisere funnene til en sammenhengende strategi orkestrert via Azure OpenAI Service.
5.	Evaluere strategien for hull eller inkonsistenser, og eventuelt initiere en ny runde med søk.
Alle disse stegene—forbedring av spørsmål, valg av kilder, iterering til den er "fornøyd" med svaret—bestemmes av modellen, ikke forhåndsskriptet av et menneske.

## Iterative løkker, verktøyintegrasjon og minne

![Tool Integration Architecture](../../../translated_images/no/tool-integration.0f569710b5c17c10.webp)

Et agentisk system baserer seg på et løkkebasert interaksjonsmønster:

- **Initialt kall:** Brukerens mål (aka. brukerprompt) presenteres for LLM.
- **Verktøy-innkalling:** Hvis modellen identifiserer manglende informasjon eller tvetydige instruksjoner, velger den et verktøy eller en hente-metode—som et vektordatabasesøk (f.eks. Azure AI Search Hybrid search over private data) eller et strukturert SQL-kall—for å hente mer kontekst.
- **Vurdering & Forbedring:** Etter å ha gjennomgått returnerte data avgjør modellen om informasjonen er tilstrekkelig. Hvis ikke forbedres spørsmålet, prøves et annet verktøy, eller tilnærmingen justeres.
- **Gjenta til fornøyd:** Denne syklusen fortsetter til modellen bestemmer at den har nok klarhet og bevis til å levere et endelig, godt begrunnet svar.
- **Minne & Tilstand:** Fordi systemet opprettholder tilstand og minne over trinn, kan det huske tidligere forsøk og deres resultater, unngå repeterende løkker og ta mer informerte beslutninger videre.

Over tid skaper dette en følelse av utviklende forståelse, som gjør at modellen kan navigere komplekse, flerstegsoppgaver uten at et menneske trenger å gripe inn eller omforme prompten konstant.

## Håndtering av feilmoduser og selvkorrigering

Agentisk RAGs autonomi inkluderer også robuste selvkorrigeringsmekanismer. Når systemet støter på blindveier—som å hente irrelevante dokumenter eller møte feilformulerte spørsmål—kan det:

- **Iterere og nyforespørre:** Istedenfor å returnere lite verdifulle svar, prøver modellen nye søkestrategier, omskriver databaseforespørsler eller ser på alternative datasett.
- **Bruke diagnostiske verktøy:** Systemet kan kalle opp flere funksjoner designet for å hjelpe til med å feilsøke resonnementstrinn eller bekrefte riktigheten av hentede data. Verktøy som Azure AI Tracing vil være viktige for å muliggjøre robust observabilitet og overvåkning.
- **Tilbakefall til menneskelig tilsyn:** For høyrisiko- eller gjentatte feilsituasjoner kan modellen markere usikkerhet og be om menneskelig veiledning. Når mennesket gir korrigerende tilbakemelding, kan modellen inkorporere denne lærdommen fremover.

Denne iterative og dynamiske tilnærmingen gjør at modellen kontinuerlig kan forbedre seg, og sikrer at den ikke bare er et engangssystem, men et som lærer av sine feil under en gitt økt.

![Self Correction Mechanism](../../../translated_images/no/self-correction.da87f3783b7f174b.webp)

## Agentgrensesnitt

Til tross for sin autonomi innen en oppgave, er Agentic RAG ikke analogt til kunstig generell intelligens. Dets "agentiske" egenskaper er begrenset til verktøyene, datakildene og retningslinjene som er gitt av menneskelige utviklere. Det kan ikke oppfinne egne verktøy eller gå utenfor domenets grenser som er satt. Det utmerker seg heller i dynamisk orkestrering av ressursene det har.
Viktige forskjeller fra mer avanserte AI-former inkluderer:

1. **Domenespesifikk autonomi:** Agentic RAG-systemer fokuserer på å oppnå brukerdefinerte mål innenfor et kjent domene, og benytter strategier som omskriving av spørsmål eller valg av verktøy for å forbedre resultater.
2. **Infrastrukturavhengighet:** Systemets evner er avhengig av verktøyene og dataene utviklerne har integrert. Det kan ikke overskride disse grensene uten menneskelig inngripen.
3. **Respekt for sikkerhetsrammer:** Etiske retningslinjer, samsvarsregler og bedriftsretningslinjer er fortsatt svært viktige. Agentens frihet er alltid begrenset av sikkerhetstiltak og overvåkningsmekanismer (forhåpentligvis?)

## Praktiske bruksområder og verdi

Agentic RAG utmerker seg i situasjoner som krever iterativ forbedring og presisjon:

1. **Korrekthet-først-miljøer:** I samsvarssjekker, regulatoriske analyser eller juridisk forskning kan den agentiske modellen gjentatte ganger verifisere fakta, konsultere flere kilder og omskrive spørsmål til den leverer et grundig gjennomgått svar.
2. **Komplekse databaseinteraksjoner:** Når man håndterer strukturerte data hvor spørringer ofte kan feile eller trenge justering, kan systemet selvstendig forbedre sine spørringer ved bruk av Azure SQL eller Microsoft Fabric OneLake, og sikre at endelig henting stemmer med brukerens intensjon.
3. **Utvidede arbeidsflyter:** Lengre økter kan utvikle seg ettersom ny informasjon dukker opp. Agentic RAG kan kontinuerlig inkorporere ny data, skifte strategier etter hvert som det lærer mer om problemområdet.

## Styring, transparens og tillit

Ettersom disse systemene blir mer autonome i sitt resonnement, er styring og transparens avgjørende:

- **Forklarbart resonnement:** Modellen kan gi en revisjonsspor av spørsmålene den stilte, kildene den konsulterte, og resonnementstrinnene den tok for å nå sin konklusjon. Verktøy som Azure AI Content Safety og Azure AI Tracing / GenAIOps kan hjelpe med å opprettholde transparens og redusere risiko.
- **Biaskontroll og balansert henting:** Utviklere kan justere hente-strategier for å sikre at balanserte, representative datakilder blir vurdert, og regelmessig revidere utdata for å oppdage bias eller skjeve mønstre ved bruk av tilpassede modeller for avanserte data science-organisasjoner som bruker Azure Machine Learning.
- **Menneskelig tilsyn og samsvar:** For sensitive oppgaver er menneskelig gjennomgang fortsatt essensiell. Agentic RAG erstatter ikke menneskelig dømmekraft i høyrisiko-beslutninger—det styrker den ved å levere mer gjennomgåtte alternativer.

Å ha verktøy som gir klar oversikt over handlinger er avgjørende. Uten dem kan det være svært vanskelig å feilsøke en flerstegsprosess. Se følgende eksempel fra Literal AI (selskapet bak Chainlit) for en Agent-kjøring:

![AgentRunExample](../../../translated_images/no/AgentRunExample.471a94bc40cbdc0c.webp)

## Konklusjon

Agentic RAG representerer en naturlig utvikling i hvordan AI-systemer håndterer komplekse, dataintensive oppgaver. Ved å adoptere et løkkebasert interaksjonsmønster, autonomt velge verktøy og forbedre spørsmål til et høykvalitetsresultat oppnås, beveger systemet seg utover statisk følg-prompt inn i en mer adaptiv, kontekstbevisst beslutningstaker. Selv om det fortsatt er bundet av menneskeskapt infrastruktur og etiske retningslinjer, gir disse agentiske evnene rikere, mer dynamiske og i siste instans mer nyttige AI-interaksjoner for både virksomheter og sluttbrukere.

### Har du flere spørsmål om Agentic RAG?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine spørsmål om AI-agenter.

## Tilleggsressurser

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementer Retrieval Augmented Generation (RAG) med Azure OpenAI Service: Lær hvordan du bruker dine egne data med Azure OpenAI Service. Denne Microsoft Learn-modulen gir en omfattende guide til implementering av RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering av generative AI-applikasjoner med Microsoft Foundry: Denne artikkelen dekker evaluering og sammenligning av modeller på offentlig tilgjengelige datasett, inkludert Agentic AI-applikasjoner og RAG-arkitekturer</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Hva er Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: En komplett guide til agentbasert Retrieval Augmented Generation – Nyheter fra generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentisk RAG: gi fart til RAG med spørring-omformulering og selv-spørring! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Legge til agentiske lag i RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Fremtiden for kunnskapassistenter: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Hvordan bygge agentiske RAG-systemer</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Bruke Microsoft Foundry Agent Service for å skalere dine AI-agenter</a>

### Akademiske Artikler

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativ forbedring med selvtilbakemelding</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Språkagenter med verbal forsterkende læring</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Store språklige modeller kan rette seg selv med verktøy-interaktiv kritikk</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentisk Retrieval-Augmented Generation: En oversikt over agentisk RAG</a>

## Røyk-testing av denne agenten (valgfritt)

Etter at du har lært å distribuere agenter i [Lesson 16](../16-deploying-scalable-agents/README.md), kan du røyk-teste `TravelRAGAgent` i denne leksjonen — for å sjekke at svarene holder seg forankret i kunnskapsbasen — med [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Se [`tests/README.md`](../tests/README.md) for hvordan du kjører det.

## Forrige leksjon

[Designmønster for verktøybruk](../04-tool-use/README.md)

## Neste leksjon

[Bygge pålitelige AI-agenter](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->