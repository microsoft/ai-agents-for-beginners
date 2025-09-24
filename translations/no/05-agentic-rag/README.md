<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T15:54:27+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "no"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.no.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klikk på bildet over for å se videoen til denne leksjonen)_

# Agentic RAG

Denne leksjonen gir en omfattende oversikt over Agentic Retrieval-Augmented Generation (Agentic RAG), et fremvoksende AI-paradigme der store språkmodeller (LLMs) autonomt planlegger sine neste steg samtidig som de henter informasjon fra eksterne kilder. I motsetning til statiske mønstre for henting og lesing, involverer Agentic RAG iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata. Systemet evaluerer resultater, forbedrer forespørsler, bruker flere verktøy om nødvendig, og fortsetter denne syklusen til en tilfredsstillende løsning er oppnådd.

## Introduksjon

Denne leksjonen vil dekke:

- **Forstå Agentic RAG:** Lær om det fremvoksende paradigmet i AI der store språkmodeller (LLMs) autonomt planlegger sine neste steg samtidig som de henter informasjon fra eksterne datakilder.
- **Forstå Iterativ Maker-Checker-stil:** Forstå loopen med iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata, designet for å forbedre nøyaktighet og håndtere feilformede forespørsler.
- **Utforsk praktiske bruksområder:** Identifiser scenarier der Agentic RAG utmerker seg, som miljøer med fokus på korrekthet, komplekse databaseinteraksjoner og utvidede arbeidsflyter.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du vite hvordan du/forstå:

- **Forstå Agentic RAG:** Lær om det fremvoksende paradigmet i AI der store språkmodeller (LLMs) autonomt planlegger sine neste steg samtidig som de henter informasjon fra eksterne datakilder.
- **Iterativ Maker-Checker-stil:** Forstå konseptet med en loop av iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata, designet for å forbedre nøyaktighet og håndtere feilformede forespørsler.
- **Eie resonneringsprosessen:** Forstå systemets evne til å eie sin resonneringsprosess, ta beslutninger om hvordan problemer skal tilnærmes uten å være avhengig av forhåndsdefinerte veier.
- **Arbeidsflyt:** Forstå hvordan en agentisk modell selvstendig bestemmer seg for å hente markedsrapporttrender, identifisere konkurrentdata, korrelere interne salgsdata, syntetisere funn og evaluere strategien.
- **Iterative looper, verktøyintegrasjon og minne:** Lær om systemets avhengighet av et loopet interaksjonsmønster, opprettholde tilstand og minne på tvers av steg for å unngå repeterende looper og ta informerte beslutninger.
- **Håndtering av feilmoduser og selvkorrigering:** Utforsk systemets robuste selvkorrigeringsmekanismer, inkludert iterasjon og nye forespørsler, bruk av diagnostiske verktøy og fallback til menneskelig tilsyn.
- **Begrensninger av autonomi:** Forstå begrensningene til Agentic RAG, med fokus på domenespesifikk autonomi, avhengighet av infrastruktur og respekt for sikkerhetsrammer.
- **Praktiske bruksområder og verdi:** Identifiser scenarier der Agentic RAG utmerker seg, som miljøer med fokus på korrekthet, komplekse databaseinteraksjoner og utvidede arbeidsflyter.
- **Styring, åpenhet og tillit:** Lær om viktigheten av styring og åpenhet, inkludert forklarbar resonnering, kontroll av skjevheter og menneskelig tilsyn.

## Hva er Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) er et fremvoksende AI-paradigme der store språkmodeller (LLMs) autonomt planlegger sine neste steg samtidig som de henter informasjon fra eksterne kilder. I motsetning til statiske mønstre for henting og lesing, involverer Agentic RAG iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata. Systemet evaluerer resultater, forbedrer forespørsler, bruker flere verktøy om nødvendig, og fortsetter denne syklusen til en tilfredsstillende løsning er oppnådd. Denne iterative “maker-checker”-stilen forbedrer nøyaktighet, håndterer feilformede forespørsler og sikrer resultater av høy kvalitet.

Systemet eier aktivt sin resonneringsprosess, omskriver mislykkede forespørsler, velger ulike metoder for henting og integrerer flere verktøy—som vektorsøk i Azure AI Search, SQL-databaser eller tilpassede API-er—før det ferdigstiller svaret. Den særegne kvaliteten til et agentisk system er dets evne til å eie sin resonneringsprosess. Tradisjonelle RAG-implementeringer er avhengige av forhåndsdefinerte veier, men et agentisk system bestemmer autonomt rekkefølgen av steg basert på kvaliteten på informasjonen det finner.

## Definere Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) er et fremvoksende paradigme innen AI-utvikling der LLMs ikke bare henter informasjon fra eksterne datakilder, men også autonomt planlegger sine neste steg. I motsetning til statiske mønstre for henting og lesing eller nøye skriptede promptsekvenser, involverer Agentic RAG en loop av iterative kall til LLM, avbrutt av verktøy- eller funksjonskall og strukturerte utdata. Ved hver vending evaluerer systemet resultatene det har oppnådd, bestemmer om det skal forbedre forespørslene, bruker flere verktøy om nødvendig, og fortsetter denne syklusen til det oppnår en tilfredsstillende løsning.

Denne iterative “maker-checker”-stilen er designet for å forbedre nøyaktighet, håndtere feilformede forespørsler til strukturerte databaser (f.eks. NL2SQL), og sikre balanserte, høykvalitetsresultater. I stedet for å stole utelukkende på nøye konstruerte promptkjeder, eier systemet aktivt sin resonneringsprosess. Det kan omskrive forespørsler som mislykkes, velge ulike metoder for henting og integrere flere verktøy—som vektorsøk i Azure AI Search, SQL-databaser eller tilpassede API-er—før det ferdigstiller svaret. Dette eliminerer behovet for overkompliserte orkestreringsrammeverk. I stedet kan en relativt enkel loop av “LLM-kall → verktøybruk → LLM-kall → …” gi sofistikerte og godt begrunnede utdata.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.no.png)

## Å eie resonneringsprosessen

Den særegne kvaliteten som gjør et system “agentisk” er dets evne til å eie sin resonneringsprosess. Tradisjonelle RAG-implementeringer er ofte avhengige av at mennesker forhåndsdefinerer en vei for modellen: en tankerekke som skisserer hva som skal hentes og når.  
Men når et system er virkelig agentisk, bestemmer det internt hvordan det skal tilnærme seg problemet. Det utfører ikke bare et skript; det bestemmer autonomt rekkefølgen av steg basert på kvaliteten på informasjonen det finner.  
For eksempel, hvis det blir bedt om å lage en produktlanseringsstrategi, stoler det ikke bare på en prompt som beskriver hele forsknings- og beslutningsprosessen. I stedet bestemmer den agentiske modellen selvstendig å:

1. Hente rapporter om nåværende markedstrender ved hjelp av Bing Web Grounding.
2. Identifisere relevant konkurrentdata ved hjelp av Azure AI Search.
3. Korrelere historiske interne salgsdata ved hjelp av Azure SQL Database.
4. Syntetisere funnene til en sammenhengende strategi orkestrert via Azure OpenAI Service.
5. Evaluere strategien for hull eller inkonsekvenser, og eventuelt starte en ny runde med henting.  
Alle disse stegene—å forbedre forespørsler, velge kilder, iterere til det er “fornøyd” med svaret—blir bestemt av modellen, ikke forhåndsskriptet av et menneske.

## Iterative looper, verktøyintegrasjon og minne

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.no.png)

Et agentisk system er avhengig av et loopet interaksjonsmønster:

- **Første kall:** Brukerens mål (dvs. brukerens prompt) presenteres for LLM.
- **Verktøybruk:** Hvis modellen identifiserer manglende informasjon eller tvetydige instruksjoner, velger den et verktøy eller en metode for henting—som en vektordatabaseforespørsel (f.eks. Azure AI Search Hybrid-søk over privat data) eller et strukturert SQL-kall—for å samle mer kontekst.
- **Vurdering og forbedring:** Etter å ha gjennomgått de returnerte dataene, bestemmer modellen om informasjonen er tilstrekkelig. Hvis ikke, forbedrer den forespørselen, prøver et annet verktøy eller justerer tilnærmingen.
- **Gjenta til fornøyd:** Denne syklusen fortsetter til modellen bestemmer at den har nok klarhet og bevis til å levere et endelig, velbegrunnet svar.
- **Minne og tilstand:** Fordi systemet opprettholder tilstand og minne på tvers av steg, kan det huske tidligere forsøk og deres utfall, unngå repeterende looper og ta mer informerte beslutninger etter hvert som det går fremover.

Over tid skaper dette en følelse av utviklende forståelse, som gjør det mulig for modellen å navigere komplekse, flertrinnsoppgaver uten at et menneske konstant må gripe inn eller omforme prompten.

## Håndtering av feilmoduser og selvkorrigering

Agentic RAGs autonomi innebærer også robuste selvkorrigeringsmekanismer. Når systemet møter blindveier—som å hente irrelevante dokumenter eller støte på feilformede forespørsler—kan det:

- **Iterere og forespørre på nytt:** I stedet for å returnere lavverdige svar, forsøker modellen nye søkestrategier, omskriver databaseforespørsler eller ser på alternative datasett.
- **Bruke diagnostiske verktøy:** Systemet kan bruke tilleggskall designet for å hjelpe det med å feilsøke resonneringsstegene eller bekrefte korrektheten av hentede data. Verktøy som Azure AI Tracing vil være viktige for å muliggjøre robust observasjon og overvåking.
- **Fallback til menneskelig tilsyn:** For oppgaver med høy risiko eller gjentatte feil, kan modellen flagge usikkerhet og be om menneskelig veiledning. Når mennesket gir korrigerende tilbakemelding, kan modellen inkorporere denne lærdommen fremover.

Denne iterative og dynamiske tilnærmingen lar modellen kontinuerlig forbedre seg, og sikrer at den ikke bare er et engangssystem, men et som lærer av sine feil i løpet av en gitt økt.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.no.png)

## Begrensninger av autonomi

Til tross for sin autonomi innenfor en oppgave, er ikke Agentic RAG det samme som kunstig generell intelligens. Dens “agentiske” evner er begrenset til verktøyene, datakildene og retningslinjene som er gitt av menneskelige utviklere. Den kan ikke finne opp sine egne verktøy eller gå utover de domenebegrensningene som er satt. I stedet utmerker den seg ved dynamisk å orkestrere ressursene som er tilgjengelige.  
Viktige forskjeller fra mer avanserte AI-former inkluderer:

1. **Domenespesifikk autonomi:** Agentic RAG-systemer er fokusert på å oppnå brukerdefinerte mål innenfor et kjent domene, og bruker strategier som omskriving av forespørsler eller verktøyvalg for å forbedre resultater.
2. **Avhengig av infrastruktur:** Systemets evner er avhengige av verktøyene og dataene som er integrert av utviklere. Det kan ikke overskride disse grensene uten menneskelig inngripen.
3. **Respekt for sikkerhetsrammer:** Etiske retningslinjer, samsvarsregler og forretningspolitikk forblir svært viktige. Agentens frihet er alltid begrenset av sikkerhetstiltak og tilsynsmekanismer (forhåpentligvis?).

## Praktiske bruksområder og verdi

Agentic RAG utmerker seg i scenarier som krever iterativ forbedring og presisjon:

1. **Miljøer med fokus på korrekthet:** I samsvarskontroller, regulatoriske analyser eller juridisk forskning kan den agentiske modellen gjentatte ganger verifisere fakta, konsultere flere kilder og omskrive forespørsler til den produserer et grundig gjennomgått svar.
2. **Komplekse databaseinteraksjoner:** Når man arbeider med strukturerte data der forespørsler ofte kan mislykkes eller trenge justering, kan systemet autonomt forbedre forespørslene sine ved hjelp av Azure SQL eller Microsoft Fabric OneLake, og sikre at den endelige henting samsvarer med brukerens intensjon.
3. **Utvidede arbeidsflyter:** Lengre økter kan utvikle seg etter hvert som ny informasjon dukker opp. Agentic RAG kan kontinuerlig inkorporere nye data og endre strategier etter hvert som den lærer mer om problemområdet.

## Styring, åpenhet og tillit

Etter hvert som disse systemene blir mer autonome i sin resonnering, er styring og åpenhet avgjørende:

- **Forklarbar resonnering:** Modellen kan gi en revisjonsspor av forespørslene den gjorde, kildene den konsulterte og resonneringsstegene den tok for å komme frem til sin konklusjon. Verktøy som Azure AI Content Safety og Azure AI Tracing / GenAIOps kan bidra til å opprettholde åpenhet og redusere risiko.
- **Kontroll av skjevheter og balansert henting:** Utviklere kan justere hentestrategier for å sikre at balanserte, representative datakilder vurderes, og regelmessig gjennomgå utdata for å oppdage skjevheter eller skjeve mønstre ved hjelp av tilpassede modeller for avanserte dataorganisasjoner som bruker Azure Machine Learning.
- **Menneskelig tilsyn og samsvar:** For sensitive oppgaver forblir menneskelig gjennomgang essensielt. Agentic RAG erstatter ikke menneskelig dømmekraft i beslutninger med høy risiko—den forsterker den ved å levere mer grundig vurderte alternativer.

Å ha verktøy som gir en klar oversikt over handlinger er essensielt. Uten dem kan det være svært vanskelig å feilsøke en flertrinnsprosess. Se følgende eksempel fra Literal AI (selskapet bak Chainlit) for en Agent-kjøring:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.no.png)

## Konklusjon

Agentic RAG representerer en naturlig utvikling i hvordan AI-systemer håndterer komplekse, dataintensive oppgaver. Ved å adoptere et loopet interaksjonsmønster, autonomt velge verktøy og forbedre forespørsler til det oppnår et høykvalitetsresultat, beveger systemet seg utover statisk prompt-etterfølgelse til å bli en mer tilpasningsdyktig, kontekstbevisst beslutningstaker. Selv om det fortsatt er begrenset av menneskedefinerte infrastrukturer og etiske retningslinjer, muliggjør disse agentiske evnene rikere, mer dynamiske og til slutt mer nyttige AI-interaksjoner for både bedrifter og sluttbrukere.

### Har du flere spørsmål om Agentic RAG?

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortimer og få svar på dine spørsmål om AI-agenter.

## Tilleggsressurser

-
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementering av Retrieval Augmented Generation (RAG) med Azure OpenAI Service: Lær hvordan du bruker dine egne data med Azure OpenAI Service. Denne Microsoft Learn-modulen gir en omfattende veiledning om implementering av RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluering av generative AI-applikasjoner med Azure AI Foundry: Denne artikkelen dekker evaluering og sammenligning av modeller på offentlige tilgjengelige datasett, inkludert Agentic AI-applikasjoner og RAG-arkitekturer</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Hva er Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: En komplett guide til agentbasert Retrieval Augmented Generation – Nyheter fra generasjon RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: gi fart til din RAG med spørringsreformulering og selvspørring! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Legge til agentiske lag til RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Fremtiden for kunnskapsassistenter: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Hvordan bygge agentiske RAG-systemer</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Bruke Azure AI Foundry Agent Service for å skalere dine AI-agenter</a>

### Akademiske artikler

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativ forbedring med selvtilbakemelding</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Språkagenter med verbal forsterkningslæring</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Store språkmodeller kan selvkorrigere med verktøy-interaktiv kritikk</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: En undersøkelse om Agentic RAG</a>

## Forrige leksjon

[Designmønster for verktøybruk](../04-tool-use/README.md)

## Neste leksjon

[Bygge pålitelige AI-agenter](../06-building-trustworthy-agents/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.